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
from good_interface.legacy import ISpec, Interface
from inspect import getfullargspec
from copy import deepcopy

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------ DATA ------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


class TestInterface1:
    """
    First Interface to test interface methods.
    Test single method
    """
    def method1(self, arg1):
        """
        First interface method
        """
        pass
ITestInterface1 = Interface(TestInterface1)


class TestInterface2:
    """
    Second Interface to test interface methods
    Adding second method to TestInterface1
    """
    def method1(self, arg1):
        """
        First interface method
        """
        pass

    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass
ITestInterface2 = Interface(TestInterface2)


class TestInterface3:
    """
    Third Interface to test interface methods
    Removing first method and just having second and third
    """
    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

    def method3(self, *args):
        """
        Third interface method
        Has varargs
        """
        pass
ITestInterface3 = Interface(TestInterface3)


class TestInterface4:
    """
    Fourth interface to test interface methods
    Having all three methods
    """
    def method1(self, arg1):
        """
        First interface method
        """
        pass

    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

    def method3(self, *args):
        """
        Third interface method
        """
        pass
ITestInterface4 = Interface(TestInterface4)


class TestClass:
    """
    Test class to test interface methods
    """
    # Example param (should not be speccable)
    param = 2

    def __init__(self):
        """
        Initialize method (should not be speccable)
        """
        pass

    def method1(self, arg1):
        """
        First class method
        """
        pass

    def method2(self, arg1, arg2):
        """
        Second class method
        """
        pass

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------ TESTS -----------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


class ISpecTest(unittest.TestCase):
    """
    Tests the ISpec class

    Author:  Anshul Kharbanda
    Created: 10 - 19 - 2017
    """
    # Manually generated specdict for TestClass
    manual_specdict = {
        'method1': getfullargspec(TestClass.method1),
        'method2': getfullargspec(TestClass.method2)
    }

    def test_speccable(self):
        """
        Tests the speccable method
        """
        self.assertTrue(ISpec.speccable(TestClass.method1))
        self.assertFalse(ISpec.speccable(TestClass.__init__))
        self.assertFalse(ISpec.speccable(TestClass.param))

    def test_specdict(self):
        """
        Tests the specdict method
        """
        # Assert that the manual specdict equals the generated specdict
        self.assertEqual(self.manual_specdict, ISpec.specdict(TestClass))

    def test_init(self):
        """
        Tests initialization
        """
        # Assert that spec of a dict equals spec of the
        # object representing the spec
        self.assertEqual(ISpec(self.manual_specdict), ISpec(TestClass))

    def test_implemented(self):
        """
        Tests implemented method
        """
        self.assertTrue(ISpec(TestInterface1).implemented(ISpec(TestClass)))
        self.assertTrue(ISpec(TestInterface2).implemented(ISpec(TestClass)))
        self.assertFalse(ISpec(TestInterface3).implemented(ISpec(TestClass)))
        self.assertFalse(ISpec(TestInterface4).implemented(ISpec(TestClass)))


class InterfaceTest(unittest.TestCase):
    """
    Tests the Interface class

    Author:  Anshul Kharbanda
    Created: 10 - 19 - 2017
    """
    def test_initialization(self):
        """
        Tests init method
        """
        self.assertEqual(ITestInterface1.__name__, 'TestInterface1')
        self.assertEqual(ITestInterface1.__spec__, ISpec(TestInterface1))

    def test_extended(self):
        """
        Tests extended method
        """
        new_name = ITestInterface3.__name__
        new_spec = deepcopy(ITestInterface1.__spec__)
        new_spec.update(ITestInterface3.__spec__)
        NewInterface = ITestInterface1.extended(ITestInterface3)
        self.assertEqual(NewInterface.__name__, new_name)
        self.assertEqual(NewInterface.__spec__, new_spec)

    def test_implemented(self):
        """
        Tests implemented method
        """
        self.assertTrue(ITestInterface1.implemented(TestClass))
        self.assertTrue(ITestInterface2.implemented(TestClass))
        self.assertFalse(ITestInterface3.implemented(TestClass))
        self.assertFalse(ITestInterface4.implemented(TestClass))

    def test_call_for_assert_classes(self):
        """
        Tests class assertion __call__
        """
        self.assertEqual(ITestInterface1(TestClass), TestClass)

    def test_call_for_assert_instance(self):
        """
        Tests instance assertion __call__
        """
        test_inst = TestClass()
        self.assertEqual(ITestInterface1(test_inst), test_inst)

    def test_call_for_assert_class_error(self):
        """
        Tests erroring class assertion __call__
        """
        with self.assertRaises(Exception): ITestInterface3(TestClass)

    def test_call_for_assert_instance_error(self):
        """
        Tests erroring instance assertion __call__
        """
        test_inst = TestClass()
        with self.assertRaises(Exception): ITestInterface3(test_inst)

    def test_call_for_extend(self):
        """
        Tests extension __call__
        """
        CallInfc = ITestInterface1(ITestInterface3)
        ExtdInfc = ITestInterface1.extended(ITestInterface3)
        self.assertEqual(CallInfc.__spec__, ExtdInfc.__spec__)
        self.assertEqual(ExtdInfc.__name__, ITestInterface3.__name__)