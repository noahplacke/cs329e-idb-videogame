from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/games/')
def games():
	return render_template('games.html')

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
