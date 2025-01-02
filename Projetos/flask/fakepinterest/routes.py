# Aqui vc vai colocar as suas rotas/caminhos dos seu site
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
from fakepinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename
# render_template: Procura uma pasta chamada templates onde tem vários arquivos html e é colocado nesse arquivo flask

#url_for: Faz com que ao invés de ele de direcionar pelo caminho que está configurado ele te direciona de acordo com a função que está nas rotas

#login_required: serve para dizer que para ele acessar um certo site ele tem que fazer login

# redirect: vai te redirecionar para alguma página

# login_user: Gerencia os logins do usuário

# logout_user: Gerencia os logouts do usuário

@app.route('/', methods=['GET', 'POST']) # Cria o caminho do link do seu site
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit(): # Se os campos do formulário foram preenchidos corretamente, de acordo com as validações configuradas.
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first() # encontrar um usuário na tabela Usuario com o mesmo email fornecido no formulário de login.
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data): # Se o usuário foi encontrado no banco de dados e se a senha fornecida no formulário está correta
            login_user(usuario) # Marca o usuario como "logado" na sessão.
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin) # Pega o arquivo html e coloca no app.route

@app.route('/criar-conta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit(): # Se o usuario clicou no botão de criar conta
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data) # criptografa a senha
        usuario = Usuario(username=formcriarconta.username.data, senha=senha, email=formcriarconta.email.data)
        database.session.add(usuario) # adiciona um usuario no banco de dados
        database.session.commit() # database.session.commit() confirma a transação e salva todas as alterações no banco de dados.
        login_user(usuario, remember=True) # autentica um usuário e iniciar uma sessão. Esse método registra o usuário como autenticado e associa a sessão do navegador com o usuário em questão.

        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criar-conta.html', form=formcriarconta)

@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required # O cliente só vai ter acesso se fazer o login
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id): # se o id do usuásio for igual ao id de acesso
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOALDER'], nome_seguro)
            arquivo.save(caminho) # salva o arquivo na pasta fotos-post

            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto) # Adiciona a foto no banco
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao).all() # Vai pegar todas as fotos só que ele vai ordenar pela data de criação da primeira até a ultima (.desc())
    return render_template('feed.html', fotos=fotos)

@app.route('/teste')
def teste():
    return 'Perfil do Usuário'