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
    Function stub object. Defines input/output behavior of function
    """
    def __init__(self, nargs, varargs=False, kwargs=False, method=False):
        """
        Initialize Stub class

        :param nargs:   Number of required input arguments
        :param varargs: True if varargs is applied
        :param kwargs:  True if kwargs is applied
        :param method:  True if spec is for method
        """
        self._nargs = nargs
        self._varargs = varargs
        self._kwargs = kwargs
        self._method = method

    def check(self, func):
        """
        Checks if given function implements the stub

        :param func: Function to test

        :return: True if the given function implements the stub
        """
        argspec = getfullargspec(func)
        return (len(argspec.args) - (1 if self._method else 0) == self._nargs) \
            and (bool(argspec.varargs) == bool(self._varargs)) \
            and (bool(argspec.varkw) == bool(self._kwargs))


def make_stub_from_func(func, method=False):
    """
    Create stub from function

    :param func: function to create stub from
    :param method: true if the function is a method

    :return: stub created from function
    """
    argspec = getfullargspec(func)
    return Stub(
        len(argspec.args) - (1 if method else 0),
        bool(argspec.varargs),
        bool(argspec.varkw),
        method)


def get_stubs(ifcs):
    """
    Return stubs of class skeleton

    :param ifcs: interface class skeleton

    :return: Dictionary of stubs in class
    """
    return {
        name: Stub(stub._nargs, stub._varargs, stub._kwargs, True) if isinstance(stub, Stub) else make_stub_from_func(stub, True)
        for name, stub in ifcs.__dict__.items()
        if isinstance(stub, Stub) or callable(stub)}
