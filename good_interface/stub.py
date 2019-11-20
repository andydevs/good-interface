"""
Good Interface

Provides the Interface class and other utilities
which can define method "interfaces" which
automatically check method implementation in
classes and objects.

Author:  Anshul Kharbanda
Created: 6 - 26 - 2018
"""
from inspect import getfullargspec


class Stub:
    """
    Method stub object. Defines input/output behavior of method
    """
    def __init__(self, nargs, varargs=False, kwargs=False):
        """
        Initialize Stub class

        :param nargs:   Number of required input arguments
        :param varargs: True if varargs is applied
        :param kwargs:  True if kwargs is applied
        """
        self._nargs = nargs
        self._varargs = varargs
        self._kwargs = kwargs

    def check(self, func):
        """
        Checks if given function implements the stub

        :param func: Function to test

        :return: True if the given function implements the stub
        """
        argspec = getfullargspec(func)
        return len(argspec.args) == self._nargs \
            and (bool(argspec.varargs) == bool(self._varargs)) \
            and (bool(argspec.varkw) == bool(self._kwargs))
