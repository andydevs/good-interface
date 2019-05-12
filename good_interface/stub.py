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

class stub:
    """
    Method stub
    """
    def __init__(self, required, varargs=False, kwargs=False, defimpl=None):
        """
        Initializes stub

        :param required: Number of required arguments
        :param varargs:  True if varargs are allowed
        :param kwargs:   True if kwargs are allowed
        :param defimpl:  Default implementation of function
        """
        self.required = required
        self.varargs  = varargs
        self.kwargs   = kwargs
        self.defimpl  = defimpl

    def valid(self, func):
        """
        True if the given function is valid according to stub

        :param func: function to check

        :return: True if the given function is valid
        """
        aspec = getfullargspec(func)
        nargs = len(aspec.args) - len(aspec.defaults or [])
        varargs = aspec.varargs is not None
        kwargs = aspec.varkw is not None or aspec.defaults is not None
        return all([
            self.required == nargs,
            self.varargs == varargs,
            self.kwargs == kwargs])
