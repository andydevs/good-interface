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

class StubValidTest(unittest.TestCase):
    """
    Test valid Method.

    Valid if all:
       1. number of args equals required
       2. varargs provided if varargs is true
       3. kwargs provided if kwargs is true
    """
    def setUp(self):
        """
        Sets up test case
        """
        self.stubs = [
            stub(required=0),
            stub(required=0, varargs=True),
            stub(required=0, kwargs=True),
            stub(required=0, varargs=True, kwargs=True),
            stub(required=3),
            stub(required=3, varargs=True),
            stub(required=3, kwargs=True),
            stub(required=3, varargs=True, kwargs=True),
            stub(required=3, defaults=2),
            stub(required=3, defaults=2, varargs=True),
            stub(required=3, defaults=2, kwargs=True),
            stub(required=3, defaults=2, varargs=True, kwargs=True)
        ]

    def test_noargs(self):
        """
        Tests function with no arguments
        """
        def func():
            pass
        self.assertTrue(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_noargs_varargs(self):
        """
        Tests function with no arguments and varargs
        """
        def func(*args):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertTrue(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_noargs_kwargs(self):
        """
        Tests function with no arguments and keyword args
        """
        def func(**kwargs):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertTrue(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_noargs_varargs_kwargs(self):
        """
        Tests function with no arguments and varargs and keyword args
        """
        def func(*args, **kwargs):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertTrue(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args(self):
        """
        Tests function with 3 arguments
        """
        def func(a,b,c):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertTrue(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_varargs(self):
        """
        Tests function with 3 arguments
        """
        def func(a,b,c, *args):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertTrue(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_kwargs(self):
        """
        Tests function with 3 arguments
        """
        def func(a,b,c, **kwargs):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertTrue(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_varargs_kwargs(self):
        """
        Tests function with 3 arguments
        """
        def func(a,b,c, *args, **kwargs):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_2defs(self):
        """
        Tests function with 3 arguments and 2 defaults
        """
        def func(a,b=2,c=3):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertTrue(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_2defs_varargs(self):
        """
        Tests function with 3 arguments and 2 defaults and varargs
        """
        def func(a, b=2, c=3, *args):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertTrue(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_2defs_kwargs(self):
        """
        Tests function with 3 arguments and 2 defaults and kwargs
        """
        def func(a, b=2, c=3, **kwargs):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertTrue(self.stubs[10].valid(func))
        self.assertFalse(self.stubs[11].valid(func))

    def test_3args_2defs_varargs_kwargs(self):
        """
        Tests function with 3 arguments and 2 defaults and varargs and kwargs
        """
        def func(a, b=2, c=3, *varargs, **kwargs):
            pass
        self.assertFalse(self.stubs[0].valid(func))
        self.assertFalse(self.stubs[1].valid(func))
        self.assertFalse(self.stubs[2].valid(func))
        self.assertFalse(self.stubs[3].valid(func))
        self.assertFalse(self.stubs[4].valid(func))
        self.assertFalse(self.stubs[5].valid(func))
        self.assertFalse(self.stubs[6].valid(func))
        self.assertFalse(self.stubs[7].valid(func))
        self.assertFalse(self.stubs[8].valid(func))
        self.assertFalse(self.stubs[9].valid(func))
        self.assertFalse(self.stubs[10].valid(func))
        self.assertTrue(self.stubs[11].valid(func))
