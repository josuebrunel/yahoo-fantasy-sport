import pdb
import logging
import unittest

from yahoo_oauth import OAuth2, OAuth1

from fantasy_sport import FantasySport
from fantasy_sport.utils import pretty_json, pretty_xml

logging.getLogger('yahoo_oauth').setLevel(logging.WARNING)

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logging.getLogger('test-fantasy-sports')

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

    def test_get_leagues(self):
        response = self.yfs.get_leagues(['238.l.627060'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

    def test_get_leagues_with_multiple_keys(self,):
        self.yfs.fmt = 'xml'
        response = self.yfs.get_leagues(('238.l.627060','238.l.627062'))
        self.yfs.fmt = 'json'
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_xml(response.content))

    def test_get_leagues_scoreboard(self):
        response = self.yfs.get_leagues_scoreboard(['238.l.627060'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

    def test_get_leagues_settings(self):
        response = self.yfs.get_leagues_settings(['238.l.627060','238.l.627062'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

    def test_get_leagues_standings(self):
        response = self.yfs.get_leagues_standings(['238.l.627060','238.l.627062'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

    def test_get_leagues_transactions(self):
        response = self.yfs.get_leagues_transactions(['238.l.627060','238.l.627062'])
        self.assertEqual(response.status_code, 200)
        logging.debug(pretty_json(response.content))

