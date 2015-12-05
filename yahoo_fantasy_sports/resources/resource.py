from abc import ABCMeta, abstractmethod


class Resource(object):
    """
    Base class for creating resources such as ``Game``, ``League``, etc...
    """
    __metaclass__ = ABCMeta
