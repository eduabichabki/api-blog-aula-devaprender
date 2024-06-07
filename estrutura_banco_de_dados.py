from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Criar um API flask
app = Flask(__name__)

#Criar uma instancia de SQL Alchemy
app.config['SECRET_KEY'] = 'colocar_algo_dificil'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

#Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

#Definir a estrutura da tabela autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

#Para rodar os proximos comandos do banco de dodos
def inicializar_banco():
    with app.app_context():

        #Executar o comando para criar o banco de dados
        db.drop_all()
        db.create_all()

        #Criar usuarios administradores
        autor = Autor(nome='Eduardo', email='eduabichabki@email.com', senha='123456', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_banco()