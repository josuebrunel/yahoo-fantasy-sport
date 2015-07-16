from __future__ import absolute_import, unicode_literals

import six
import abc
import json

from xml.etree import cElementTree as ctree

@six.add_metaclass(abc.ABCMeta)
class Base(object):
    """Base class for Roster and Player
    """

    @abc.abstractmethod
    def xml_builder(self,):
        raise NotImplementedError

    @abc.abstractmethod
    def json_builder(self,):
        raise NotImplementedError
   
    def to_json(self,):
        """Return object as a json string
        """
        return json.dumps(self.json, ensure_ascii=True).encode('ascii')

    def to_xml(self,):
        """Return object as a xml string
        """
        return ctree.tostring(self.xml)


class Roster(Base):
    """Roster class
    """

    def __init__(self, players, week=None, date=None):
        """Initialize a roster class
        """
        super(Base, self).__init__()

        self.players = players

        if week:
            self.coverage = week
            self.coverage_type = 'week'
        else:
            self.coverage = date
            self.coverage_type = 'date'

        self.json_builder()
        self.xml_builder()

    def xml_builder(self,):
        """Convert object to xml
        """
        content = ctree.Element('fantasy_content')
        roster = ctree.SubElement(content, 'roster')

        coverage_type = ctree.SubElement(roster, 'coverage_type')
        coverage_type.text = self.coverage_type

        coverage = ctree.SubElement(roster, self.coverage_type)
        coverage.text = self.coverage

        players = ctree.SubElement(roster, 'players')
        for player in self.players :
            players.append(player.xml)

        self.xml = content

    def json_builder(self,):
        """Convert object to json
        """
        self.json = {
            'fantasy_content':{
                'roster':{
                    'coverage_type': self.coverage_type,
                    self.coverage_type : self.coverage,
                    'players': [ player.json for player in self.players ]
                }
            }
        }
        return self.json
    

class Player(Base):
    """player class
    - player_key
    - position
    """

    def __init__(self, player_key, position):
        """Initialize a player object
        """
        super(Base, self).__init__()

        self.player_key = player_key
        self.position = position
        self.xml_builder()
        self.json_builder()

    def xml_builder(self,):
        """Convert object into a xml object
        """
        player = ctree.Element('player')
        for key in sorted(vars(self).keys()):
            tag = ctree.SubElement(player, key)
            tag.text = vars(self).get(key)
        
        self.xml = player
        return self.xml

    def json_builder(self, ):
        """Kind of convert object to json
        """
        self.json = {
            'player_key': self.player_key,
            'position': self.position
        }

        return self.json

