# Aqui vc vai definir o seu site/app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager # gerencia os logins
from flask_bcrypt import Bcrypt # gerencia as criptografias

app = Flask(__name__) # Cria o seu site
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' # Vai criar uma pasta onde o banco de dados vai ficar armazenado
app.config['SECRET_KEY'] = '972b3b25bc2cab9643cce52e1e6ab719c1a7ed2e8c290cb4b18fdbba5000' # import secrets -> print(secrets.token_hex(n° de caracteres)): chave de segurança do seu site
app.config['UPLOAD_FOALDER'] = 'static/fotos-posts' # Onde as fotos postadas vão ser armazenadas

database = SQLAlchemy(app) # Cria um banco de dados
bcrypt = Bcrypt(app) # Vai criar a criptografia
login_manager = LoginManager(app)
login_manager.login_view = 'homepage' # Para onde o usuario vai ser redirecionado caso ele não tiver feito o login (função nos routes)

from fakepinterest import routes