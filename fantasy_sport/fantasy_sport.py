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

    def _check_token_validity(self,):
        """Check wether or not the access token is still valid, if not, renews it
        """
        if not self.oauth.token_is_valid():
            self.oauth.refresh_access_token
        return True

    def _get(self, uri):
        """
        """

        if not self.oauth.oauth.base_url :
            self.oauth.oauth.base_url = self.url
        
        self._check_token_validity()

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

    def _build_uri(self, resources, keys, sub=None):
        """Build uri
        """
        uri = "{0}={1}".format(resources, self._format_resources_key(keys))
        if sub and isinstance(sub, str) :
            uri += "/{0}".format(sub)
        if sub and not isinstance(sub, str):
            uri += ";out={0}".format(','.join([e for e in sub]))

        if self.use_login:
            uri = self._add_login(uri)

        return uri

    def get_collections(self, resource_type, resource_ids, sub_resources):
        """Generic method to get collections
        """
        uri = self._build_uri(resource_type, resource_ids, sub=sub_resources)
        response = self._get(uri)
        return response

    #################################
    #
    #           GAMES
    #
    #################################

    def get_games_info(self, game_keys):
        """Return game info
        >>> yfs.get_games_info('mlb')
        """
        uri = self._build_uri('games;game_keys', game_keys)
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
        uri = self._build_uri('leagues;league_keys',league_keys)
        response = self._get(uri)
        return response

    def get_leagues_teams(self, league_keys):
        """Return leagues teams
        >>> yfs.get_leagues_teams(['238.l.627062'])
        """
        uri = self._build_uri('leagues;league_keys', league_keys, sub='teams')
        response = self._get(uri)
        return response

    def get_leagues_scoreboard(self, league_keys, week=None):
        """Return leagues scoreboard
        >>> yfs.get_leagues_scoreboard(['league_key'])
        """
        uri = self._build_uri('leagues;league_keys',league_keys, sub='scoreboard')

        if week:
            uri += ';week={0}'.format(week)

        response = self._get(uri)
        return response

    def get_leagues_settings(self, league_keys):
        """Return leagues settings
        >>> yfs.get_leagues_settings(['238.l.627062','238.l.627062'])
        """
        uri = self._build_uri('leagues;league_keys', league_keys, sub='settings')
        response = self._get(uri)
        return response

    def get_leagues_standings(self, league_keys):
        """Return leagues settings
        >>> yfs.get_leagues_settings(['238.l.627062','238.l.627062'])
        """
        uri = self._build_uri('leagues;league_keys', league_keys, sub='standings')
        response = self._get(uri)
        return response

    def get_leagues_transactions(self, league_keys):
        """Return leagues settings
        >>> yfs.get_leagues_transactions(['238.l.627062'])
        """
        uri = self._build_uri('leagues;league_keys', league_keys, sub='transactions')
        response = self._get(uri)
        return response

    def get_leagues_draftresults(self, league_keys):
        """Return leagues draftresults
        >>> yfs.get_leagues_draftresults(['238.l.627062'])
        """
        uri = self._build_uri('leagues;league_keys', league_keys, sub='draftresults')
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

