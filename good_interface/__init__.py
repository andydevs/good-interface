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
from copy import deepcopy


class ISpec(dict):
    """
    Interface Spec. Contains a set of method specs for the created object.

    Author:  Anshul Kharbanda
    Created: 10 - 19 - 2017
    """
    @staticmethod
    def speccable(meth):
        """
        Returns true if the given method is speccable, or recognised as part of an
        interface spec and checked for when checking an instance for implementation

        :param meth: the method being checked

        :return: true if the given method is speccable
        """
        DONT_SPEC = ('__init__', '__new__')
        return callable(meth) and meth.__name__ not in DONT_SPEC

    @staticmethod
    def specdict(item):
        """
        Returns the dictionary of method specs in the given item

        :param item: the item to spec

        :return: the dictionary of method specs in the given item
        """
        return {
            entry[0]:getfullargspec(entry[1])
            for entry in item.__dict__.items()
            if ISpec.speccable(entry[1])
        }

    def __init__(self, item):
        """
        Initializes the spec with the given item

        :param item: the item to spec (or the spec if is dict)
        """
        super(ISpec, self).__init__(
            item if type(item) is dict else ISpec.specdict(item)
        )

    def implemented(self, other):
        """
        Returns true if the given spec is implemented in the other spec

        :param other: the other spec being checked

        :Returns true if the given spec is implemented in the other spec
        """
        return all(item in other.items() for item in self.items())


class Interface:
    """
    A set of methods to be implemented in a class

    Author:  Anshul Kharbanda
    Created 10 - 19 - 2017
    """
    def __init__(self, infc):
        """
        Creates the interface

        :param infc: the interface object to analyze
        """
        self.__name__ = infc.__name__
        self.__spec__ = ISpec(infc)

    def extended(self, infc):
        """
        Extends the given interface

        :param infc: the interface to extend

        :return: extended interface
        """
        nifc = deepcopy(infc)
        nifc.__spec__.update(self.__spec__)
        return nifc

    def implemented(self, impl):
        """
        Returns true if the interface is implemented in the given class

        :param impl: the implementing class to check

        :return: true if the interface is implemented in the given class
        """
        return self.__spec__.implemented(ISpec(impl))

    def __call__(self, obj):
        """
        Asserts that the given class or object implements the Interface else errors

        :param impl: the class to check

        :return: the class or object if it implements the interface

        :raises Exception: if class does not implement the Interface
        """
        if type(obj) is Interface: return self.extended(obj)
        elif self.implemented(obj) or self.implemented(type(obj)): return obj
        else: raise Exception('{obj} does not implement {infc}'.format(obj=obj, infc=self.__name__))

    def __repr__(self):
        """
        Returns the string representation of the interface

        :return: the string representation of the Interface
        """
        return '<interface {}>'.format(self.__name__)