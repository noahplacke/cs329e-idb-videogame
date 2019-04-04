from flask import render_template
from create_db import app, db, Game, Genre, create_games

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/games/')
def games():
  #games = db.session.query(Game).all()
  games = db.session.query(Game).join((Genre, Game.genres)).all()
  return render_template('games2.html', games = games)

@app.route('/genres/')
def genres():
	return render_template('genres.html')

@app.route('/companies/')
def companies():
	return render_template('companies.html')
	
@app.route('/about/')
def about():
	return render_template('about.html')

if __name__ == "__main__":
  app.run()
