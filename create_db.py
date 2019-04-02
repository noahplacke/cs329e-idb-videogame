import json
#from models import app, db, Game, Genre, Company
from models import app, db, Genre, Game, Company

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_games():
  games = load_json('games.json')

  for oneGame in games['Games']:

    game_id = oneGame['id']
    name = oneGame['name']
    rating = oneGame['rating']
    summary = oneGame['summary']
    url = oneGame['url']
    genres = oneGame['genres']
    companies = oneGame['involved_companies']

    newGame = Game(game_id = game_id, name = name, rating = rating, summary = summary, url = url, genres = genres, companies = companies)
    # After I create the book, I can then add it to my session.
    db.session.add(newGame)
    # commit the session to my DB.
    db.session.commit()

create_games()

def create_genres():
    genres = load_json('genres.json')

    for oneGenre in genres['Genres']:
        name = oneGenre['name']
        id = oneGenre['id']
        url = oneGenre['url']


        newGenre = Genre(id = id, name = name, url = url)

        # After I create the book, I can then add it to my session.
        db.session.add(newGenre)
        # commit the session to my DB.
        db.session.commit()

create_genres()

"""
  company_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(250), nullable = True)
  description = db.Column(db.String(1000), nullable = True)
  logo = db.Column(db.Integer, nullable = True)
  country = db.Column(db.Integer, nullable = True)
  games = db.Column(db.String(1000), nullable = True)
"""
def create_companies():
  companies = load_json('companies.json')

  for oneCompany in companies['Companies']:
    company_id = oneCompany['id']
    name = oneCompany['name']
    description = oneCompany['description']
    logo = oneCompany['logo']
    games = oneCompany['developed']


    newCompany = Company(company_id = company_id, name = name, description = description, logo = logo, games = games)

    # After I create the book, I can then add it to my session.
    db.session.add(newCompany)
    # commit the session to my DB.
    db.session.commit()

create_companies()
# end of create_db.py
