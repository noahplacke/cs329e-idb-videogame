import os
import sys
import unittest
from models import db, Game, Genre

class DBTestCases(unittest.TestCase):
  def test_self_1(self):
    self.assertTrue(True)
	
  def test_game_insert_1(self):
    
    s = Game(game_id='20', name = 'The Game')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '20').one()
    self.assertEqual(str(r.game_id), '20')
    self.assertEqual(str(r.name), 'The Game')
    db.session.query(Game).filter_by(game_id = '20').delete()
    db.session.commit()
	
  def test_game_insert_2(self):
    
    s = Game(game_id='99', name = '99th Game', rating = '4.3', companies = 'Rockstar Games')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '99').one()
    self.assertEqual(str(r.game_id), '99')
    self.assertEqual(str(r.rating), '4.3')
    self.assertEqual(str(r.companies), 'Rockstar Games')
    db.session.query(Game).filter_by(game_id = '99').delete()
    db.session.commit()

  def test_genre_insert_1(self):
    
    s = Genre(genre_id='9999', name = 'GenreTest', url = 'google.com')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Genre).filter_by(genre_id = '9999').one()
    self.assertEqual(str(r.genre_id), '9999')
    self.assertEqual(str(r.name), 'GenreTest')
    self.assertEqual(str(r.url), 'google.com')
    db.session.query(Genre).filter_by(genre_id = '9999').delete()
    db.session.commit()
    
	
if __name__ == '__main__':
  unittest.main() 
