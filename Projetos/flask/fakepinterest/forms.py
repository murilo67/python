# Aqui você vai criar os formulários do seu site
from flask_wtf import FlaskForm # Gerencia formulários
from wtforms import StringField, PasswordField, SubmitField, FileField # Cria uma área de email, senha, um botão de envio e uma área de arquivo
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # Vai definir respectivamente a validação de campos como a obrigatóriedade, se vai ser email, se tal campo tem que ser igual a tal campo, o n° de caracteres e a mensagem de erro
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('Seu e-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Sua senha', validators=[DataRequired()])
    botao_enviar = SubmitField('Fazer login')

class FormCriarConta(FlaskForm): # Tem que ter entre parênteses o 'FlaskForm'
    email = StringField('Seu e-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome de usuário', validators=[DataRequired()])
    senha = PasswordField('Sua senha', validators=[DataRequired(), Length(8)])
    confirmacao_senha = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('senha')])
    botao_enviar = SubmitField('Criar conta')

    def validate_email(self, email): # validate_... e o campo que vc quer validar e dentro do parentese ela tem que receber tal coisa que vc quer validar
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('Email já cadastrado, faça login novamente para continuar')
        
class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botao_enviar = SubmitField('Enviar')

# StringField(placeholder, validators=[]) -> Campo de texto/email