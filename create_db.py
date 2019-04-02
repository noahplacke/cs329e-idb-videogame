import json
#from models import app, db, Game, Genre, Company
from models import app, db, Genre, Game

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
def create_companies():
    companies = load_json('companies.json')

    for oneCompany in companies['Companies']:
        title = oneCompany['title']
        id = oneCompany['id']
        games = oneCompany['games']
        genres = oneCompany['genres']


        newCompany = Company(title = title, id = id, games = games, genres = genres)

        # After I create the book, I can then add it to my session.
        db.session.add(newCompany)
        # commit the session to my DB.
        db.session.commit()

create_companies()
"""
# end of create_db.py
