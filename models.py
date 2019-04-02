# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:abc123@localhost:5433/gamesdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)
"""
class Game(db.Model):
	__tablename__ = 'games'

	title = db.Column(db.String(80), nullable = False)
	id = db.Column(db.Integer, primary_key = True)
	genre = db.Column(db.String(80), nullable = False)
	company = db.Column(db.String(80), nullable = False)
	rating = db.Column(db.String(80), nullable = True)
"""
class Genre(db.Model):
	__tablename__ = 'genres'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(250), nullable = False)
	url = db.Column(db.String(500), nullable = False)
"""
class Company(db.Model):
	__tablename__ = 'companies'

	title = db.Column(db.String(80), nullable = False)
	id = db.Column(db.Integer, primary_key = True)
	games = db.Column(db.String(250), nullable = False)
	genres = db.Column(db.String(250), nullable = False)
"""

db.drop_all()
db.create_all()
print("tables created")
# End of models.py
