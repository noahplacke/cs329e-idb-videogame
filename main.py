from flask import render_template, request
from create_db import app, db, Game, Genre, Company, create_games
import subprocess

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/games/')
def games():
  field = request.args.get('field')
  direction = request.args.get('direction')
  if field == "name":
    games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.name.asc()).all()
  else:
    games = db.session.query(Game).join((Genre, Game.genres)).all()
  return render_template('games.html', games = games)

@app.route('/genres/')
def genres():
  genres = db.session.query(Genre).join((Game, Genre.games)).all()
  return render_template('genres.html', genres = genres)

@app.route('/companies/')
def companies():
  companies = db.session.query(Company).join((Game, Company.games)).all()
  return render_template('companies.html', companies = companies)
	
@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/test/')
def test():
    p = subprocess.Popen(["coverage", "run", "--branch", "test.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
    out, err = p.communicate()
    output=err+out
    output = output.decode("utf-8") #convert from byte type to string type
    
    return render_template('test.html', output = "<br/>".join(output.split("\n")))

if __name__ == "__main__":
  app.run()
