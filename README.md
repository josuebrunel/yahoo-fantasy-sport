# Yahoo Fantasy Sport API

[![Build Status](https://travis-ci.org/josuebrunel/yahoo-fantasy-sport.svg?branch=master)](https://travis-ci.org/josuebrunel/yahoo-fantasy-sport) 
[![Documentation Status](https://readthedocs.org/projects/yahoo-fantasy-sport/badge/?version=latest)](https://readthedocs.org/projects/yahoo-fantasy-sport/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/josuebrunel/yahoo-fantasy-sport/badge.svg?branch=master)](https://coveralls.io/r/josuebrunel/yahoo-fantasy-sport?branch=master)
[![Code Health](https://landscape.io/github/josuebrunel/yahoo-fantasy-sport/master/landscape.svg?style=flat)](https://landscape.io/github/josuebrunel/yahoo-fantasy-sport/master)

## Authors

* [Josue Kouka](https://github.com/josuebrunel)
* [Paul Singman](https://github.com/unpairestgood)

## Installation

```shell
$ pip install yahoo-fantasy-sport
```

## Quickstart

```python
>>> from yahoo_oauth import OAuth1
>>> oauth = OAuth1(None, None, from_file='oauth.json', base_url='http://fantasysports.yahooapis.com/fantasy/v2/')
>>> from fantasy_sport import FantasySport
>>> yfs = FantasySport(oauth, fmt='json')
```

### Games Resources

### Leagues Resources

### Players Resources

## How to contribute

- Open an issue
- Fork the repository
- Make your changes
- Test your changes 
- Add yourself into the AUTHORS.txt file
- Submit a pull request
