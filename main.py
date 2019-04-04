from flask import render_template, request
from create_db import app, db, Game, Genre, create_games
import subprocess

@app.route('/')
def index():
	return render_template('index.html')



@app.route('/games/')
def games():
  field = request.args.get('field')
  direction = request.args.get('direction')

  if field == "name":
    if direction == "desc":
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.name.desc()).all()
    else:
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.name.asc()).all()

  elif field == "summary":
    if direction == "desc":
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.summary.desc()).all()
    else:
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.summary.asc()).all()

  elif field == "genre":
    if direction == "desc":
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.genre.desc()).all()
    else:
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.genre.asc()).all()

  elif field == "company":
    if direction == "desc":
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.companies.desc()).all()
    else:
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.companies.asc()).all()

  elif field == "rating":
    if direction == "desc":
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.rating.desc()).all()
    else:
      games = db.session.query(Game).join((Genre, Game.genres)).order_by(Game.rating.asc()).all()

  else:
    games = db.session.query(Game).join((Genre, Game.genres)).all()

  return render_template('games.html', games = games)




@app.route('/genres/')
def genres():
  genres = db.session.query(Genre).join((Game, Genre.games)).all()
  return render_template('genres.html', genres = genres)

@app.route('/companies/')
def companies():
	return render_template('companies.html')
	
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
