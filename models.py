# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:abc123@localhost:5432/gamesdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

"""
game_genre_bridge = Table('association', Base.metaData,
  Column('game_id', Integer, ForeignKey('games.id')),
  Column('genres_id', Integer, ForeignKey('genres.id'))
)
"""

class Game(db.Model):
  __tablename__ = 'games'

  game_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  rating = db.Column(db.Float(5), nullable = True)
  summary = db.Column(db.String(5000), nullable = True)
  url = db.Column(db.String(250), nullable = True)
  genres = db.Column(db.String(80), nullable = True)
  companies = db.Column(db.String(250), nullable = True)

class Genre(db.Model):
	__tablename__ = 'genres'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(250), nullable = False)
	url = db.Column(db.String(500), nullable = False)

class Company(db.Model):
  __tablename__ = 'companies'

  company_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(250), nullable = True)
  description = db.Column(db.String(5000), nullable = True)
  logo = db.Column(db.Integer, nullable = True)
  country = db.Column(db.Integer, nullable = True)
  games = db.Column(db.String(1000), nullable = True)

db.drop_all()
db.create_all()
print("tables created")
# End of models.py
