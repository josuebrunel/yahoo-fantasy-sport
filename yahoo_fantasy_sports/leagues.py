from __future__ import absolute_import, division, print_function

from . import Collection
from .utils import build_uri, yfs_request


class Leagues(Collection):
    """
    Leagues collection.
    """

    collection = "leagues"

    def __init__(self, oauth, data):
        self._oauth = oauth
        self._game_key = data['game_key']
        self._game_id = data['game_id']
        self._code = data['code']
        self._name = data['name']
        self._season = data['season']

    def _meta(self):
        uri = build_uri(self.resource, resource_key=self._game_key)
        return yfs_request(self._oauth, uri)

    @property
    def game_key(self):
        return self._game_key

    @property
    def game_id(self):
        return self._game_id

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        response = self._meta()
        return response['fantasy_content']['game'][0]['url']

    @property
    def season(self):
        return self._season

    @property
    def is_registration_over(self):
        response = self._meta()
        return response['fantasy_content']['game'][0]['is_registration_over']

    @property
    def type(self):
        response = self._meta()
        return response['fantasy_content']['game'][0]['type']

    @property
    def game_weeks(self):
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='game_weeks')
        response = yfs_request(self._oauth, uri)
        return response['fantasy_content']['game'][1]['game_weeks']

    @property
    def stat_categories(self):
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='stat_categories')
        response = yfs_request(self._oauth, uri)
        return \
            response['fantasy_content']['game'][1]['stat_categories']['stats']

    @property
    def position_types(self):
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='position_types')
        response = yfs_request(self._oauth, uri)
        return response['fantasy_content']['game'][1]['position_types']

    @property
    def roster_positions(self):
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='roster_positions')
        response = yfs_request(self._oauth, uri)
        return response['fantasy_content']['game'][1]['roster_positions']
