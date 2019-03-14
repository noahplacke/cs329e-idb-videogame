#-----------------------------------------
# app2.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template




app = Flask(__name__)





@app.route('/')
def index():
	return render_template('games.html')





'''
@app.route('/book/')
def book():
	return render_template('book.html')
'''






if __name__ == "__main__":
	app.run()
