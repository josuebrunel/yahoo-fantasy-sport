import pdb
import logging
import unittest

from yahoo_oauth import OAuth2, OAuth1

from fantasy_sport import FantasySport
from fantasy_sport.utils import pretty_json, pretty_xml

logging.getLogger('yahoo_oauth').setLevel(logging.WARNING)

class TestFantasySport(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)

    def test_get_games_info(self,):
        response = self.yfs.get_games_info(['nfl'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))
        
    def test_get_games_info_with_login(self,):
        response = self.yfs.get_games_info(['mlb'], use_login=True)
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

    def test_get_league(self):
        response = self.yfs.get_leagues(['238.l.627060'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

    def test_get_league_with_multiple_keys(self,):
        self.yfs.fmt = 'xml'
        response = self.yfs.get_leagues(('238.l.627060','238.l.627062'))
        self.yfs.fmt = 'json'
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_xml(response.content))
