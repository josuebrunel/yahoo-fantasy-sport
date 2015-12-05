from resource import Resource


class Game(Resource):
    """
    Game resource, containing subresource invocations.
    """

    def meta(game_key):
        """
        Provides metadata about a queried game.

        :param game_key: Game-key or game-code, *ex. ``'nba'``, ``'mlb'``,
            ``323``, ``238``*.
        :type game_key: str or int
        """
        pass
