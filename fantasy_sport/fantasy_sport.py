from __future__ import absolute_import


class FantasySport(object):
    """FantasySport Class
    """

    url = 'http://fantasysports.yahooapis.com/fantasy/v2/'

    def __init__(self, oauth, fmt=None, use_login=False):
        """Initialize a FantasySport object
        """
        self.oauth = oauth
        self.fmt = 'json' if not fmt else fmt  # JSON as default format
        self.use_login = use_login


    def __repr__(self,):
        return "<{0}> <{1}>".format(self.url, self.fmt)

    def _get(self, uri):
        """
        """

        if not self.oauth.oauth.base_url :
            self.oauth.oauth.base_url = self.url

        if not self.oauth.token_is_valid():
            self.oauth.refresh_access_token

        response = self.oauth.session.get(uri, params={'format': self.fmt})

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

    def _format_resources_key(self, keys):
        """Format resources keys 
        """
        return ','.join(str(e) for e in keys)

    def get_games_info(self, game_keys, use_login=False):
        """Return game info
        >>> yfs.get_games_info('mlb')
        """
        uri = 'games;game_keys={0}'.format(self._format_resources_key(game_keys))

        if use_login:
            uri = self._add_login(uri)
        response = self._get(uri)

        return response

    ####################################
    #
    #           LEAGUES 
    #
    ####################################
    def get_leagues(self, league_keys):
        """Return league data
        >>> yfs.get_leagues(['league_key'])
        """     
        uri = 'leagues;league_keys={0}'.format(self._format_resources_key(league_keys))

        response = self._get(uri)

        return response

    def get_leagues_scoreboard(self, league_keys):
        """Return leagues scoreboard
        >>> yfs.get_leagues_scoreboard(['league_key'])
        """
        uri = 'leagues;league_keys={0}/scoreboard'.format(self._format_resources_key(league_keys))
        response = self._get(uri)
        return response

    ###################################
    #
    #           PLAYERS
    #
    ###################################

    ###################################
    #
    #           TEAMS
    #   
    ###################################

