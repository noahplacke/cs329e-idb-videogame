from flask import render_template
from create_db import app, db, Game, Genre, create_games
import subprocess

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
