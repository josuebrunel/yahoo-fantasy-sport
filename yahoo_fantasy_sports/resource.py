from __future__ import absolute_import, division, print_function

from abc import ABCMeta
from six import add_metaclass


@add_metaclass(ABCMeta)
class Resource(object):
    """
    Base class for creating resources such as ``Game``, ``League``, etc...
    """
