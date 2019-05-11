"""
Good Interface

Provides the Interface class and other utilities
which can define method "interfaces" which
automatically check method implementation in
classes and objects.

Author:  Anshul Kharbanda
Created: 6 - 26 - 2018
"""
import unittest
from good_interface.stub import stub

class StubConstructorTest(unittest.TestCase):
    """
    Test constructor

    1 - required (required)
    2 - varargs (optional, default: False)
    3 - kwargs (optional, default: False)
    4 - defimpl (optional, default: None)
    """
    def test_required(self):
        """
        Tests required input
        """
        # Errors if required not given
        with self.assertRaises(Exception):
            mystub = stub()

        # Sets internal variable required to 3
        mystub = stub(required=3)
        self.assertEqual(3, mystub.required)

        # Is first argument of stub
        mystub = stub(3)
        self.assertEqual(3, mystub.required)

    def test_varargs(self):
        """
        Tests varargs input
        """
        # Sets internal variable varargs to True
        mystub = stub(required=3, varargs=True)
        self.assertEqual(True, mystub.varargs)

        # Defaults to false if varargs not given
        mystub = stub(3)
        self.assertEqual(False, mystub.varargs)

        # Is second argument of stub
        mystub = stub(3, True)
        self.assertEqual(True, mystub.varargs)

    def test_kwargs(self):
        """
        Tests kwargs input
        """
        # Sets internal variable kwargs to True
        mystub = stub(required=3, kwargs=True)
        self.assertEqual(True, mystub.kwargs)

        # Defaults to false if kwargs not given
        mystub = stub(3)
        self.assertEqual(False, mystub.kwargs)

        # Is third argument of stub
        mystub = stub(3, False, True)
        self.assertEqual(True, mystub.kwargs)

    def test_defimpl(self):
        """
        Tests defimpl input
        """
        def myfunc():
            pass

        # Sets internal variable defimpl to myfunc
        mystub = stub(required=3, defimpl=myfunc)
        self.assertEqual(myfunc, mystub.defimpl)

        # Defaults to None if defimpl not given
        mystub = stub(3)
        self.assertEqual(None, mystub.defimpl)

        # Is fourth argument of stub
        mystub = stub(3, False, False, myfunc)
        self.assertEqual(myfunc, mystub.defimpl)
