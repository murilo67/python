# Aqui você vai criar a estrutura do banco de dados
from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin # Diz qual classe vai gerenciar a estrutura de login

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))
# Essa função é usada pelo Flask-Login para carregar um usuário autenticado a partir de seu ID, que foi armazenado na sessão. Quando o Flask-Login precisar identificar o usuário atualmente logado, ele chamará essa função, passando o id_usuario como argumento.

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True) 
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'),nullable=False)

# database.Integer: Diz que aquele característica vai ser um inteiro
# database.String: Diz que aquela característica vai ser uma string
# database.relationship('Foto'): A característica se relaciona com a tabela de fotos
# primary_key=True: Uma chave primária é um identificador único para cada registro na tabela.
# nullable=False: Vc é obrigado a colocar alguma coisa
# unique=True: Vai ser único
# backref='usuario': O parâmetro backref (abreviação de back reference) define um relacionamento reverso. Ele cria automaticamente um atributo chamado usuario no modelo Foto, permitindo que você acesse o usuário associado a uma determinada foto.
# default='default.png': Se nenhum valor for fornecido para a coluna imagem ao criar um registro no banco de dados, o SQLAlchemy automaticamente define o valor como 'default.png'.
# database.DateTime: Vai definir uma data no banco de dados
# default=database.utcnow(): Caso não tiver data na base de dados ele vai definir a data no momento em que a foto foi postada
# database.Column: Cria uma coluna para a base de dados
# database.ForeignKey('usuario.id'): Essa coluna será usada como chave estrangeira para referenciar a coluna id da tabela usuario.
# lazy=True: Quando lazy=True, as fotos associadas ao usuário só serão carregadas quando você acessar explicitamente usuario.fotos.