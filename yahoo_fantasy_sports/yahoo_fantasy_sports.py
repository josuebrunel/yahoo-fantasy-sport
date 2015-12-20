from __future__ import absolute_import, division, print_function

import json

from . import GamesFactory
from .utils import base_url, yfs_request


class YahooFantasySports(object):
    """
    Interact with the Yahoo Fantasy Sports Servers.

    :param oauth: OAuth1 instance connected to the Yahoo servers.
    :type oauth: yahoo_oauth.Oauth1
    :param fmt: Format of the response. Either 'json' or 'xml'. Defaults
        to 'json'.
    :type fmt: str
    :param use_login:
    :type use_login: bool
    """

    def __init__(self, oauth, fmt='json', use_login=False):
        self.oauth = oauth
        self.fmt = fmt
        self.use_login = use_login
        self.games = GamesFactory(oauth)

    def __repr__(self):
        return "<{0}> <{1}>".format(base_url, self.fmt)

    def test_uri(self, uri):
        print(json.dumps(yfs_request(self.oauth, base_url + uri),
              indent=4))
