"""
Good Interface

Provides the Interface class and other utilities
which can define method "interfaces" which
automatically check method implementation in
classes and objects.

Author:  Anshul Kharbanda
Created: 6 - 26 - 2018
"""
from .stub import get_stubs
from copy import deepcopy


class Interface:
    """
    A set of method stubs to be implemented in a class

    Author:  Anshul Kharbanda
    Created  11 - 21 - 2019
    """
    def __init__(self, infc):
        """
        Initialize interface

        :param infc: interface class skeleton
        """
        self.__name__ = infc.__name__
        self._stubs = get_stubs(infc)

    def extended(self, infc):
        """
        Extends the given interface

        :param infc: interface to extend

        :return: extended interface
        """
        nifc = deepcopy(infc)
        nifc._stubs.update(self._stubs)
        return nifc

    def implemented(self, impl):
        """
        Returns true if the interface is implemented in the given class

        :param impl: the implementing class to check

        :return: true if the interface is implemented in the given class
        """
        return all(
            name in impl.__dict__ and stub.check(impl.__dict__[name])
            for name, stub in self._stubs.items())

    def __call__(self, obj):
        """
        If object is an interface, returns interface extended with this one.
        Else asserts that obj or class implements the interface else errors

        :param obj: the object/class to check (or interface to extend)

        :return: the class or object if interface is implemented, or the extended interface.
        """
        if isinstance(obj, Interface):
            return self.extended(obj)
        elif self.implemented(obj) or self.implemented(type(obj)):
            return obj
        else:
            # TODO: Create custom exception type
            raise Exception(f'{obj} does not implement {self}')

    def __repr__(self):
        """
        Returns the string representation of the interface

        :return: string representation of the interface
        """
        return f'<interface {self.__name__}>'
