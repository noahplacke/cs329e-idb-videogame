import json
#from models import app, db, Game, Genre, Company
from models import app, db, Genre, Game, Company, game_genres, game_companies

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# channel1.subscribers.append(user1)
# genre1.games.append(game1)
# game1.genres.append(genre1)

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

    newGame = Game(game_id = game_id, name = name, rating = rating, summary = summary, url = url)
    db.session.add(newGame)
    db.session.commit()

    for genre_id in genres:
      statement = game_genres.insert().values(game_id = game_id, genre_id = genre_id)
      db.session.execute(statement)
      db.session.commit()

    for company_id in companies:
      try:
        statement = game_companies.insert().values(game_id = game_id, company_id = company_id)
        db.session.execute(statement)
        db.session.commit()
        print("succeeded for", game_id, company_id)
      except:
        print("failed for", game_id, company_id)
        db.session.rollback()

def create_genres():
    genres = load_json('genres.json')

    for oneGenre in genres['Genres']:
        name = oneGenre['name']
        id = oneGenre['id']
        url = oneGenre['url']


        newGenre = Genre(genre_id = id, name = name, url = url)

        # After I create the book, I can then add it to my session.
        db.session.add(newGenre)
        # commit the session to my DB.
        db.session.commit()

def create_companies():
  companies = load_json('companies.json')

  for oneCompany in companies['Companies']:
    company_id = oneCompany['id']
    name = oneCompany['name']

    description = ''
    if 'description' in oneCompany:
      description = oneCompany['description']

    logo = 0
    if 'logo' in oneCompany:
      logo = oneCompany['logo']

    newCompany = Company(company_id = company_id, name = name, description = description, logo = logo)

    # After I create the book, I can then add it to my session.
    db.session.add(newCompany)
    # commit the session to my DB.
    db.session.commit()


create_genres()
print("genres done")
create_companies()
print("companies done")
create_games()
print("games done")
# end of create_db.py
