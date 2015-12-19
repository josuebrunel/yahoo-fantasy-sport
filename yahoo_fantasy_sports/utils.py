import json

from requests import HTTPError
from xml.dom import minidom


base_url = 'http://fantasysports.yahooapis.com/fantasy/v2'


def pretty_json(data):
    """Return a pretty formatted json
    """
    data = json.loads(data.decode('utf-8'))
    return json.dumps(data, indent=4, sort_keys=True)


def pretty_xml(data):
    """Return a pretty formated xml
    """
    parsed_string = minidom.parseString(data.decode('utf-8'))
    return parsed_string.toprettyxml(indent='\t', encoding='utf-8')


def _check_token_validity(oauth):
    """
    Checks if access token is valid. If not, renews the access token.

    :param oauth: OAuth1 instace connected to the Yahoo servers.
    :type oauth: yahoo_oauth.Oauth1
    """
    if not oauth.token_is_valid():
        oauth.refresh_access_token()


def yfs_request(oauth, uri):
    """
    Sends an request with the given URI and returns the response.

    :param oauth: OAuth1 instance connected to the Yahoo servers.
    :type oauth: yahoo_oauth.Oauth1
    :param uri: Requested URI.
    :type uri: str
    :returns: Response from request
    :rtype: HTTP response as a JSON object
    :raises HTTPError: If response contains a non-200 code
    """
    if not oauth.oauth.base_url:
        oauth.oauth.base_url = base_url

    _check_token_validity(oauth)
    response = oauth.session.get(uri, params={'format': 'json'})

    try:
        response.raise_for_status()
    except HTTPError as h:
        msg = h.message + '\n' + response.json()['error']['description']
        raise HTTPError(msg)

    return response.json()


def _format_resources_key(keys):
    return ','.join(str(e) for e in keys)


def build_uri(resource, parameters=None, resource_key=None, sub=None):
    """
    Builds up the URI.
    """
    uri = base_url
    uri += "/{0}".format(resource)

    if resource_key:
        uri += "/{0}".format(resource_key)

    if parameters:
        for key, val in parameters.iteritems():
            uri += ";{0}={1}".format(key, val)

    if sub:
        uri += "/{0}".format(sub)

    return uri
