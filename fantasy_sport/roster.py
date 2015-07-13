from __future__ import absolute_import

import json
from xml.etree import cElementTree as ctree

class Roster(object):
    pass

class Player(object):
    """Roster player class
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
        self.json = json.dumps({
            'player_key': self.player_key,
            'position': self.position
        }, sort_keys=True)

        return self.json

    def to_json(self,):
        """Return object as a json string
        """
        return json.loads(self.json)


    def to_xml(self):
        """Return object as a xml string
        """
        return ctree.tostring(self.xml)

