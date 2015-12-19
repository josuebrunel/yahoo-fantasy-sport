from __future__ import absolute_import, division, print_function

from . import Resource
from . import Collection
from . import YahooFantasySportsError
from .utils import build_uri, yfs_request

import arrow
import pdb


class GamesFactory(object):
    """
    Factory class for creating Games collections or Game resource objects.
    """

    def __init__(self, oauth):
        self._oauth = oauth

    def __call__(self, *game_keys):
        # at least one game_key must be supplied
        if not game_keys:
            raise YahooFantasySportsError(
                "'game_keys' must be supplied")

        # make sure that each game_key is either a string or integer
        for key in game_keys:
            if not isinstance(key, str) and not isinstance(key, int):
                raise KeyError(
                    "'{0}' must be either a string or integer".format(key))

        if len(game_keys) == 1:
            return Game(self._oauth, *game_keys)
        else:
            return Games(self._oauth, *game_keys)


class Games(Collection):
    """
    Games Collection.
    """
    collection = "games"

    def __init__(self, oauth, *game_keys):
        self._oauth = oauth
        self._games = {}

        for key in game_keys:
            if isinstance(key, str):
                game = Game(oauth, key)
            else:
                game = Game(oauth, str(key))
            self._games[int(game.game_key)] = game

        self._last_updated = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')

    def __repr__(self):
        return "<{0} {1}>".format(
                self.__class__.__name__, str(self._games))

    def __getitem__(self, key):
        return self._games[key]

    def filter(self, is_available=None, game_types=None, game_codes=None,
               seasons=None):
        filtered_game_keys = []

        for key, game in self._games.iteritems():
            if is_available and not game.is_available:
                continue

            if game_types and game.type not in game_types:
                continue

            if game_codes and game.code not in game_codes:
                continue

            if seasons and game.season not in seasons:
                continue

            filtered_game_keys.append(key)

        return Games(self._oauth, *filtered_game_keys)

    def refresh(self):
        """
        Refreshes the entire object to contain the latest data from the Yahoo
        servers.
        """
        for game in self._games:
            game.refresh()

    @property
    def games(self):
        return self._games.keys()

    @property
    def last_updated(self):
        return self._last_updated


class Game(Resource):
    """
    Game Resource
    """
    resource = "game"

    def __init__(self, oauth, game_key):
        self._oauth = oauth
        self._game_key = game_key
        self.refresh()

    def refresh(self):
        """
        Refreshes the entire object to contain the latest data from the Yahoo
        servers.
        """
        self._refresh_meta()
        self._refresh_game_weeks()
        self._refresh_stat_categories()
        self._refresh_position_types()
        self._refresh_roster_positions()
        self._refresh_is_available()
        self._last_updated = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')

    def _refresh_meta(self):
        uri = build_uri(self.resource, resource_key=self._game_key)
        metadata = yfs_request(self._oauth, uri)['fantasy_content']['game'][0]
        self._game_key = metadata['game_key']
        self._game_id = metadata['game_id']
        self._code = metadata['code']
        self._name = metadata['name']
        self._url = metadata['url']
        self._season = metadata['season']
        self._is_registration_over = metadata['is_registration_over']
        self._type = metadata['type']

    def _refresh_game_weeks(self):
        self._game_weeks = {}
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='game_weeks')
        weeks = yfs_request(self._oauth, uri)['fantasy_content']['game'][1]
        weeks = weeks['game_weeks']

        for number, week in weeks.iteritems():
            # skip 'count' field
            if number == 'count':
                continue

            self._game_weeks[number] = {
                'start': week['game_week']['start'],
                'end': week['game_week']['end']
            }

    def _refresh_stat_categories(self):
        self._stats = {}
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='stat_categories')
        stats = yfs_request(self._oauth, uri)['fantasy_content']['game'][1]
        stats = stats['stat_categories']['stats']

        for stat in stats:
            if 'position_types' in stat['stat']:
                self._stats[stat['stat']['stat_id']] = {
                    'sort_order': stat['stat']['sort_order'],
                    'display_name': stat['stat']['display_name'],
                    'name': stat['stat']['name'],
                    'position_types': stat['stat']['position_types']
                }
            else:
                self._stats[stat['stat']['stat_id']] = {
                    'sort_order': stat['stat']['sort_order'],
                    'display_name': stat['stat']['display_name'],
                    'name': stat['stat']['name']
                }

    def _refresh_position_types(self):
        self._position_types = {}
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='position_types')
        position_types = yfs_request(self._oauth, uri)['fantasy_content']
        position_types = position_types['game'][1]['position_types']

        for position_type in position_types:
            self._position_types[position_type['position_type']['type']] = \
                position_type['position_type']['display_name']

    def _refresh_roster_positions(self):
        self._roster_positions = {}
        uri = build_uri(self.resource, resource_key=self._game_key,
                        sub='roster_positions')
        roster_positions = yfs_request(self._oauth, uri)['fantasy_content']
        roster_positions = roster_positions['game'][1]['roster_positions']

        for roster_position in roster_positions:
            rp = roster_position['roster_position']
            if 'position_type' in rp:
                self._roster_positions[rp['abbreviation']] = {
                    'position': rp['position'],
                    'display_name': rp['display_name'],
                    'position_type': rp['position_type']
                }
            else:
                self._roster_positions[rp['abbreviation']] = {
                    'position': rp['position'],
                    'display_name': rp['display_name'],
                }

    def _refresh_is_available(self):
        uri = build_uri(self.resource + 's',
                        parameters={'game_keys': self._game_key,
                                    'is_available': 1})
        response = \
            yfs_request(self._oauth, uri)['fantasy_content']['games']
        self._is_available = True if response else False

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
        return self._url

    @property
    def season(self):
        return self._season

    @property
    def is_registration_over(self):
        return self._is_registration_over

    @property
    def type(self):
        return self._type

    @property
    def game_weeks(self):
        return self._game_weeks

    @property
    def stat_categories(self):
        return self._stat_categories

    @property
    def position_types(self):
        return self._position_types

    @property
    def roster_positions(self):
        return self._roster_types

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_updated(self):
        return self._last_updated
