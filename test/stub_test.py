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
import good_interface.stub


class StubTest(unittest.TestCase):
    def test_check(self):
        # Test stubs
        stub1 = good_interface.stub.Stub(3)
        stub2 = good_interface.stub.Stub(2)
        stub3 = good_interface.stub.Stub(2, varargs=True)
        stub4 = good_interface.stub.Stub(1, varargs=True, kwargs=True)

        # Test Functions
        def testFunc1(a, b, c): pass
        def testFunc2(a, b): pass
        def testFunc3(a, b, *c): pass
        def testFunc4(a, *b, **c): pass

        # Test for function 1
        self.assertTrue(stub1.check(testFunc1))
        self.assertFalse(stub2.check(testFunc1))
        self.assertFalse(stub3.check(testFunc1))
        self.assertFalse(stub4.check(testFunc1))

        # Test for function 2
        self.assertFalse(stub1.check(testFunc2))
        self.assertTrue(stub2.check(testFunc2))
        self.assertFalse(stub3.check(testFunc2))
        self.assertFalse(stub4.check(testFunc2))

        # Test for function 3
        self.assertFalse(stub1.check(testFunc3))
        self.assertFalse(stub2.check(testFunc3))
        self.assertTrue(stub3.check(testFunc3))
        self.assertFalse(stub4.check(testFunc3))

        # Test for function 4
        self.assertFalse(stub1.check(testFunc4))
        self.assertFalse(stub2.check(testFunc4))
        self.assertFalse(stub3.check(testFunc4))
        self.assertTrue(stub4.check(testFunc4))