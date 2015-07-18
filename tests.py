import pdb
import json
import logging
import unittest

from xml.etree import cElementTree as ctree

from yahoo_oauth import OAuth1

from fantasy_sport import FantasySport
from fantasy_sport.roster import Player, Roster
from fantasy_sport.utils import pretty_json, pretty_xml

logging.getLogger('yahoo_oauth').setLevel(logging.WARNING)

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logging.getLogger('test-fantasy-sports')

class TestFantasySportGame(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)
    
    def test_get_games_info(self,):
        response = self.yfs.get_games_info(['346'])
        #response = self.yfs.get_games_info(['nfl'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_games_withleague(self,):
        response = self.yfs.get_games_info(['328'], leagues='328.l.56628')
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))
        
    def test_get_games_withplayer(self,):
        response = self.yfs.get_games_info(['328'], players='328.p.8180')
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))
        
    def test_get_games_with_login_teams(self,):
        self.yfs.use_login = True
        response = self.yfs.get_games_info(['346'], teams=True)
        self.yfs.use_login = False
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))          
        
    def test_get_games_info_with_login(self,):
        self.yfs.use_login = True
        response = self.yfs.get_games_info(['mlb'])
        self.yfs.use_login = False
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
class TestFantasySportLeague(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)

    def test_get_leagues(self):
        response = self.yfs.get_leagues(['346.l.1328'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_with_multiple_keys(self,):
        self.yfs.fmt = 'xml'
        response = self.yfs.get_leagues(('238.l.627060','238.l.627062'))
        self.yfs.fmt = 'json'
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_xml(response.content))

    def test_get_leagues_scoreboard(self):
        response = self.yfs.get_leagues_scoreboard(['238.l.627060'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_scoreboard_week_2(self):
        response = self.yfs.get_leagues_scoreboard(['238.l.178574'], week=2)
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_settings(self):
        response = self.yfs.get_leagues_settings(['238.l.627060','238.l.627062'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_standings(self):
        response = self.yfs.get_leagues_standings(['346.l.1328'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))
        
    def test_get_leagues_standings_withteam_androsterplayers(self):
        response = self.yfs.get_leagues_standings(['346.l.1328'], teams='roster', players='ownership')
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_transactions(self):
        response = self.yfs.get_leagues_transactions(['238.l.627060','238.l.627062'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_teams(self,):
        response = self.yfs.get_leagues_teams(['238.l.627060'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_leagues_draftresults(self,):
        response = self.yfs.get_leagues_draftresults(['238.l.627060'])
        self.assertEqual(response.status_code, 200)
        #logging.debug(pretty_json(response.content))

    def test_get_collections(self,):
        response = self.yfs.get_collections('leagues;league_keys', ['238.l.627060','238.l.627062'],['settings','standings'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
class TestFantasySportPlayer(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)
        
    def test_get_players(self,):
        response = self.yfs.get_players(['223.p.5479'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_playerswithfilter(self,):
        response = self.yfs.get_players(['346.p.8180', '346.p.8544'], filters='position=P')
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_players_stats(self,):
        response = self.yfs.get_players_stats(['223.p.5479'], week=3)
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)    
        
    def test_get_players_draft_analysis(self,):
        response = self.yfs.get_players_draft_analysis(['44.p.6619'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
    
    def test_get_players_percent_owned(self,):
        response = self.yfs.get_players_percent_owned(['253.p.6619'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
class TestFantasySportTeam(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)
        
    def test_get_teams(self,):
        response = self.yfs.get_teams(['346.l.1328.t.12'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_players(self,):
        response = self.yfs.get_teams_players(['346.l.1328.t.12'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_stats(self,):
        response = self.yfs.get_teams_stats(['238.l.627062.t.1'], week=10)
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_standings(self,):
        response = self.yfs.get_teams_standings(['346.l.1328.t.12'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_roster(self,):
        response = self.yfs.get_teams_roster(['346.l.1328.t.12'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)

    #def test_get_teams_roster_with_filter(self,):
    #    response = self.yfs.get_teams_roster(['346.l.1328.t.12'], players='draft_analysis', filters='position=3B')
    #    #logging.debug(pretty_json(response.content))
    #    self.assertEqual(response.status_code, 200)
        
    def test_get_teams_roster_week(self,):
        response = self.yfs.get_teams_roster(['223.l.431.t.9'], week=1)
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_roster_weekplayer(self,):
        response = self.yfs.get_teams_roster(['223.l.431.t.9'], week=1, players='draft_analysis')
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)    
                
    def test_get_teams_roster_players(self,):
        response = self.yfs.get_teams_roster(['346.l.1328.t.12'], players='draft_analysis')
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_roster_filter(self,):
        response = self.yfs.get_teams_roster(['346.l.1328.t.12'], filters='position=3B')
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
   
    def test_get_teams_draftresults(self,):
        response = self.yfs.get_teams_draftresults(['346.l.1328.t.12'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_teams_matchups(self,):
        response = self.yfs.get_teams_matchups(['238.l.627062.t.1'], weeks=['1,2'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)

class TestFantasySportRoster(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json', base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)

    def test_get_roster_players(self,):
        response = self.yfs.get_roster_players(['346.l.1328.t.12'])
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)

    def test_get_roster_players_by_week(self,):
        response = self.yfs.get_roster_players(['346.l.1328.t.12'], week=10)
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        
    def test_get_roster_players_by_date(self,):
        response = self.yfs.get_roster_players(['346.l.1328.t.12'], date='2011-05-01')
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)   

    #def test_set_roster_players(self,):
    #    response = self.yfs.set_roster_players(['346.l.1328.t.12'])
    #    self.assertEqual(response.status_code, 200)
        

class TestFantasySportTransaction(unittest.TestCase):

    def setUp(self,):
        oauth = OAuth1(None, None, from_file='oauth.json',base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
        self.yfs = FantasySport(oauth)
        
    def test_get_transactions(self,):
        response = self.yfs.get_transactions(['346.l.1328.tr.100'], players='draft_analysis')
        #logging.debug(pretty_json(response.content))
        self.assertEqual(response.status_code, 200)
        

class TestPlayer(unittest.TestCase):

    def setUp(self,):
        self.player = Player('242.p.8332','WR')

    def test_player_in_xml(self,):
        expected = b'<player><player_key>242.p.8332</player_key><position>WR</position></player>'
        logging.debug(pretty_xml(self.player.to_xml()))
        self.assertEqual(expected, self.player.to_xml())

    def test_player_in_json(self,):
        expected = {"player_key": "242.p.8332","position":"WR"}
        logging.debug(pretty_json(self.player.to_json()))
        self.assertEqual(expected, self.player.json)


class TestRoster(unittest.TestCase):

    def setUp(self,):
        players = [Player('242.p.8332', 'WR'), Player('242.p.8334','LR')]
        self.roster = Roster(players, date='2015-01-01')

    def test_roster_in_json(self,):
        expected = {
            'fantasy_content': {
                'roster': {
                    'coverage_type':'date',
                    'date':'2015-01-01',
                    'players':[
                        {"player_key": "242.p.8332","position":"WR"},
                        {"player_key": "242.p.8334","position":"LR"}
                    ]
                }
            }
        }
        logging.debug(pretty_json(self.roster.to_json()))
        self.assertEqual(expected, self.roster.json)

    def test_roster_in_xml(self,):
        expected = b'<fantasy_content><roster><coverage_type>date</coverage_type><date>2015-01-01</date><players><player><player_key>242.p.8332</player_key><position>WR</position></player><player><player_key>242.p.8334</player_key><position>LR</position></player></players></roster></fantasy_content>'
        logging.debug(pretty_xml(self.roster.to_xml()))
        self.assertEqual(expected, self.roster.to_xml())
