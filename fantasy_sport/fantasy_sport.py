from __future__ import absolute_import


class FantasySport(object):
    """FantasySport Class
    """

    url = 'http://fantasysports.yahooapis.com/fantasy/v2/'

    def __init__(self, oauth, resource=None, use_login=False):
        """Initialize a FantasySport object
        """
        self.oauth = oauth
        self.use_login = use_login


    def __repr__(self,):
        return ""

    def _get(self, uri):
        """
        """

        if not self.oauth.oauth.base_url :
            self.oauth.oauth.base_url = self.url

        if not self.oauth.token_is_valid():
            self.oauth.refresh_access_token

        response = self.oauth.session.get(uri)

        return response

    def _post(self, uri, data={}):
        """
        """
        pass

    def _add_login(self, uri):
        """Add users;use_login=1/ to the uri
        """
        uri = "users;use_login=1/{0}".format(uri)

        return uri

    def get_games_info(self, game_keys, use_login=False):
        """Return game info
        >>> yfs.get_game_info('mlb')
        """
        uri = 'games;game_keys={0}'.format(game_keys)

        if use_login:
            uri = self._add_login(uri)
        response = self._get(uri)

        return response

    def get_league(self, league_keys):
        """Return league data
        >>> yfs.get_league(['league_key'])
        """     
        uri = 'leagues;league_keys={0}'.format(league_keys)

        response = self._get(uri)

        return response

