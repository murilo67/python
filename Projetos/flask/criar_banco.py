# Não precisa ser colocado no seu projeto final
from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

with app.app_context(): # Cria um 'contexto' para o banco de dados, coisa que é exigida pelo sql-alchemy
    database.create_all() # Cria o banco de dados