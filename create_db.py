import json
#from models import app, db, Game, Genre, Company
from models import app, db, Genre

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

"""
def create_games():
    games = load_json('games.json')

    for oneGame in games['Games']:
        title = oneGame['title']
        id = oneGame['id']
        genre = oneGame['genre']
        company = oneGame['company']
        rating = oneGame['rating']


        newGame = Game(title = title, id = id, genre = genre, company = company, rating = rating)

        # After I create the book, I can then add it to my session.
        db.session.add(newGame)
        # commit the session to my DB.
        db.session.commit()

create_games()
"""

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
