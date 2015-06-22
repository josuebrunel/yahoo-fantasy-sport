from __future__ import absolute_import


class FantasySport(object):
    """FantasySport Class
    """

    url = 'http://fantasysports.yahooapis.com/fantasy/v2/'

    def __init__(self, oauth, resource=None):
        """Initialize a FantasySport object
        """
        self.oauth = oauth


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

    def get_game_info(self, game):
        """Return game info
        >>> yfs.get_game_info('mlb')
        """
        uri = 'games;games_keys={0}'.format(game)

        response = self._get(uri)

        return response

    def get_league(self, league_keys):
        """Return league data
        >>> yfs.get_league(['league_key'])
        """     
        uri = 'leagues;league_keys={0}'.format(league_keys)

        response = self._get(uri)

        return response

