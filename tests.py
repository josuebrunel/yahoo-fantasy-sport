import pdb
import unittest

from yahoo_oauth import OAuth2

from fantasy_sports import FantasySport

class TestFantasySports(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth2(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)

    def test_get_games_info(self,):
        response = self.yfs.get_games_info('mlb')
        self.assertEqual(response.status_code, 200)
        
    def test_get_games_info_with_login(self,):
        response = self.yfs.get_games_info('mlb', use_login=True)
        self.assertEqual(response.status_code, 200)

    def test_get_league(self):
        response = self.yfs.get_league('238.l.627060')
        self.assertEqual(response.status_code, 200)
