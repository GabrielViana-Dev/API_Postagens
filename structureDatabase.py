from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Criar um API flask
app = Flask(__name__)

#Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

#Definir a estrutura da tabela postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

#Definir a estrutura da tabela autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

#Executar o comando para criar o bando de dados
with app.app_context():
    db.drop_all()
    db.create_all()

    #Criar usuários administradores
    autor = Autor(nome='Gabriel', email='vianagabriel427@gmail.com',
                   senha='123456', admin=True)
    db.session.add(autor)
    db.session.commit()