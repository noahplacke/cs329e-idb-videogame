from flask import render_template, request
from create_db import app, db, Game, Genre, Company, create_games
import subprocess

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/games/')
@app.route('/games/<game_id>')
def games(game_id = None):
  if game_id is not None:
    game = db.session.query(Game).filter(Game.game_id == (int(game_id))).join((Genre, Game.genres)).join((Company, Game.companies)).first()
    return render_template('game_details.html', game = game)

  games = db.session.query(Game).join((Genre, Game.genres)).join((Company, Game.companies)).all()

  return render_template('games.html', games = games)




@app.route('/genres/')
def genres():
  field = request.args.get('field')
  direction = request.args.get('direction')

  if field == "name":
    if direction == "desc":
      genres = db.session.query(Genre).join((Game, Genre.games)).all()
    else:
      genres = db.session.query(Genre).join((Game, Genre.games)).all()

  elif field == "description":
    if direction == "desc":
      genres = db.session.query(Genre).join((Game, Genre.games)).all()
    else:
      genres = db.session.query(Genre).join((Game, Genre.games)).all()

  elif field == "games":
    if direction == "desc":
      genres = db.session.query(Genre).join((Game, Genre.games)).all()
    else:
      genres = db.session.query(Genre).join((Game, Genre.games)).all()

  elif field == "url":
    if direction == "desc":
      genres = db.session.query(Genre).join((Game, Genre.games)).all()
    else:
      genres = db.session.query(Genre).join((Game, Genre.games)).all()

  else:
    genres = db.session.query(Genre).join((Game, Genre.games)).all()
  return render_template('genres.html', genres = genres)





@app.route('/companies/')
def companies():
  field = request.args.get('field')
  direction = request.args.get('direction')

  if field == "name":
    if direction == "desc":
      companies = db.session.query(Company).join((Game, Company.games)).all()
    else:
      companies = db.session.query(Company).join((Game, Company.games)).all()

  elif field == "description":
    if direction == "desc":
      companies = db.session.query(Company).join((Game, Company.games)).all()
    else:
      companies = db.session.query(Company).join((Game, Company.games)).all()

  elif field == "games":
    if direction == "desc":
      companies = db.session.query(Company).join((Game, Company.games)).all()
    else:
      companies = db.session.query(Company).join((Game, Company.games)).all()

  elif field == "country":
    if direction == "desc":
      companies = db.session.query(Company).join((Game, Company.games)).all()
    else:
      companies = db.session.query(Company).join((Game, Company.games)).all()

  elif field == "date_founded":
    if direction == "desc":
      companies = db.session.query(Company).join((Game, Company.games)).all()
    else:
      companies = db.session.query(Company).join((Game, Company.games)).all()

  else:
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
