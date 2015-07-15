from __future__ import absolute_import, unicode_literals

import json
from xml.etree import cElementTree as ctree

class Roster(object):
    """Roster class
    """

    def __init__(self, players, week=None, date=None):
        """Initialize a roster class
        """
        self.players = players

        if week:
            self.coverage = week
            self.coverage_type = 'week'
        else:
            self.coverage = date
            self.coverage_type = 'date'

        self.__json_builder()

    def __json_builder(self,):
        """Convert object to json
        """
        self.json = {
            'fantasy_content':{
                'roster':{
                    'coverage_type': self.coverage_type,
                    self.coverage_type : self.coverage,
                }
            }
        }

        #self.json = json.dumps(data, ensure_ascii=True).encode('ascii')

class Player(object):
    """player class
    - player_key
    - position
    """

    def __init__(self, player_key, position):
        """Initialize a player object
        """
        self.player_key = player_key
        self.position = position
        self.__xml_builder()
        self.__json_builder()

    def __xml_builder(self,):
        """Convert object into a xml object
        """
        player = ctree.Element('player')
        #for key, value in vars(self).items():
        for key in sorted(vars(self).keys()):
            tag = ctree.SubElement(player, key)
            #tag.text = value
            tag.text = vars(self).get(key)
        
        self.xml = player
        return self.xml

    def __json_builder(self, ):
        """Kind of convert object to json
        """
        self.json = {
            'player_key': self.player_key,
            'position': self.position
        }

        return self.json

    def to_json(self,):
        """Return object as a json string
        """
        return json.dumps(self.json).encode('ascii')


    def to_xml(self):
        """Return object as a xml string
        """
        return ctree.tostring(self.xml)

