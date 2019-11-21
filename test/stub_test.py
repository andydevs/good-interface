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


# Test Functions


def test_func_1(a, b, c):
    pass


def test_func_2(a, b):
    pass


def test_func_3(a, b, *c):
    pass


def test_func_4(a, *b, **c):
    pass


class TestClass:
    def test_meth_1(self, a, b):
        pass

    def test_meth_2(self, a, b, *c):
        pass

    def test_meth_3(self, a, b, *c, **d):
        pass


class TestInterface:
    meth1 = good_interface.stub.Stub(4, varargs=True)

    def meth2(self, a, b, c, *d, **e):
        pass

    def meth3(self, a, b):
        pass


class StubTest(unittest.TestCase):
    def setUp(self):
        # Test stubs
        self.stub1  = good_interface.stub.Stub(3)
        self.stub2  = good_interface.stub.Stub(2)
        self.stub3  = good_interface.stub.Stub(2, varargs=True)
        self.stub4  = good_interface.stub.Stub(1, varargs=True, kwargs=True)
        self.stubm1 = good_interface.stub.Stub(2, method=True)
        self.stubm2 = good_interface.stub.Stub(2, varargs=True, method=True)
        self.stubm3 = good_interface.stub.Stub(2, varargs=True, kwargs=True, method=True)

    def test_stub_check(self):
        # Test for function 1
        self.assertTrue(self.stub1.check(test_func_1))
        self.assertFalse(self.stub2.check(test_func_1))
        self.assertFalse(self.stub3.check(test_func_1))
        self.assertFalse(self.stub4.check(test_func_1))

        # Test for function 2
        self.assertFalse(self.stub1.check(test_func_2))
        self.assertTrue(self.stub2.check(test_func_2))
        self.assertFalse(self.stub3.check(test_func_2))
        self.assertFalse(self.stub4.check(test_func_2))

        # Test for function 3
        self.assertFalse(self.stub1.check(test_func_3))
        self.assertFalse(self.stub2.check(test_func_3))
        self.assertTrue(self.stub3.check(test_func_3))
        self.assertFalse(self.stub4.check(test_func_3))

        # Test for function 4
        self.assertFalse(self.stub1.check(test_func_4))
        self.assertFalse(self.stub2.check(test_func_4))
        self.assertFalse(self.stub3.check(test_func_4))
        self.assertTrue(self.stub4.check(test_func_4))

    def test_stub_check_meth(self):
        # Test for method 1
        self.assertTrue(self.stubm1.check(TestClass.test_meth_1))
        self.assertFalse(self.stubm2.check(TestClass.test_meth_1))
        self.assertFalse(self.stubm3.check(TestClass.test_meth_1))

        # Test for method 2
        self.assertFalse(self.stubm1.check(TestClass.test_meth_2))
        self.assertTrue(self.stubm2.check(TestClass.test_meth_2))
        self.assertFalse(self.stubm3.check(TestClass.test_meth_2))

        # Test for method 3
        self.assertFalse(self.stubm1.check(TestClass.test_meth_3))
        self.assertFalse(self.stubm2.check(TestClass.test_meth_3))
        self.assertTrue(self.stubm3.check(TestClass.test_meth_3))

    def test_make_stub_from_func(self):
        # Test for function 1
        stub = good_interface.stub.make_stub_from_func(test_func_1)
        self.assertEqual(stub._nargs, self.stub1._nargs)
        self.assertEqual(stub._varargs, self.stub1._varargs)
        self.assertEqual(stub._kwargs, self.stub1._kwargs)

        # Test for function 2
        stub = good_interface.stub.make_stub_from_func(test_func_2)
        self.assertEqual(stub._nargs, self.stub2._nargs)
        self.assertEqual(stub._varargs, self.stub2._varargs)
        self.assertEqual(stub._kwargs, self.stub2._kwargs)

        # Test for function 3
        stub = good_interface.stub.make_stub_from_func(test_func_3)
        self.assertEqual(stub._nargs, self.stub3._nargs)
        self.assertEqual(stub._varargs, self.stub3._varargs)
        self.assertEqual(stub._kwargs, self.stub3._kwargs)

        # Test for function 4
        stub = good_interface.stub.make_stub_from_func(test_func_4)
        self.assertEqual(stub._nargs, self.stub4._nargs)
        self.assertEqual(stub._varargs, self.stub4._varargs)
        self.assertEqual(stub._kwargs, self.stub4._kwargs)

    def test_get_stubs(self):
        stub1 = good_interface.stub.Stub(4, varargs=True, method=True)
        stub2 = good_interface.stub.Stub(3, varargs=True, kwargs=True, method=True)
        stub3 = good_interface.stub.Stub(2, method=True)

        stubs = good_interface.stub.get_stubs(TestInterface)

        self.assertIn('meth1', stubs)
        self.assertEqual(stub1._nargs, stubs['meth1']._nargs)
        self.assertEqual(stub1._varargs, stubs['meth1']._varargs)
        self.assertEqual(stub1._kwargs, stubs['meth1']._kwargs)

        self.assertIn('meth2', stubs)
        self.assertEqual(stub2._nargs, stubs['meth2']._nargs)
        self.assertEqual(stub2._varargs, stubs['meth2']._varargs)
        self.assertEqual(stub2._kwargs, stubs['meth2']._kwargs)

        self.assertIn('meth3', stubs)
        self.assertEqual(stub3._nargs, stubs['meth3']._nargs)
        self.assertEqual(stub3._varargs, stubs['meth3']._varargs)
        self.assertEqual(stub3._kwargs, stubs['meth3']._kwargs)
