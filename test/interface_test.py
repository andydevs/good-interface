import unittest
from good_interface import Interface


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------ DATA ------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


@Interface
class ITestInterface1:
    def meth1(self):
        pass

    def meth4(self, a, b):
        pass

    def meth5(self, a, *b):
        pass

    def meth6(self, a, **c):
        pass

    def meth7(self, a, b, c, *d, **e):
        pass


@Interface
class ITestInterface2:
    def meth2(self, *a):
        pass


@Interface
class ITestInterface3:
    def meth1(self):
        pass

    def meth3(self, **c):
        pass


class TestClass:
    def meth1(self):
        pass

    def meth4(self, a, b):
        pass

    def meth5(self, a, *b):
        pass

    def meth6(self, a, **c):
        pass

    def meth7(self, a, b, c, *d, **e):
        pass


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------ TESTS -----------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


class InterfaceTest(unittest.TestCase):
    """
    Tests the Interface class

    Author:  Anshul Kharbanda
    Created: 10 - 19 - 2017
    """
    def custom_assert_method_stub(self, infc, name, nargs, varargs, kwargs):
        self.assertIn(name, infc._stubs)
        self.assertEqual(infc._stubs[name]._nargs, nargs)
        self.assertIs(infc._stubs[name]._varargs, varargs)
        self.assertIs(infc._stubs[name]._kwargs, kwargs)
        self.assertTrue(infc._stubs[name]._method)

    def test_initialization(self):
        """
        Tests init method
        """
        # Test interface instance
        self.assertIsInstance(ITestInterface1, Interface)
        self.assertEqual(ITestInterface1.__name__, 'ITestInterface1')
        self.assertIsInstance(ITestInterface2, Interface)
        self.assertEqual(ITestInterface2.__name__, 'ITestInterface2')
        self.assertIsInstance(ITestInterface3, Interface)
        self.assertEqual(ITestInterface3.__name__, 'ITestInterface3')

        # Test methods
        self.custom_assert_method_stub(ITestInterface1, 'meth1', 0, False, False)
        self.custom_assert_method_stub(ITestInterface1, 'meth4', 2, False, False)
        self.custom_assert_method_stub(ITestInterface1, 'meth5', 1, True, False)
        self.custom_assert_method_stub(ITestInterface1, 'meth6', 1, False, True)
        self.custom_assert_method_stub(ITestInterface1, 'meth7', 3, True, True)
        self.custom_assert_method_stub(ITestInterface2, 'meth2', 0, True, False)
        self.custom_assert_method_stub(ITestInterface3, 'meth1', 0, False, False)
        self.custom_assert_method_stub(ITestInterface3, 'meth3', 0, False, True)

    def test_extended(self):
        """
        Tests extended method
        """
        with self.subTest(extending='ITestInterface2'):
            Extinf = ITestInterface1.extended(ITestInterface2)
            self.assertIsInstance(Extinf, Interface)
            self.assertEqual(Extinf.__name__, 'ITestInterface2')
            self.custom_assert_method_stub(Extinf, 'meth1', 0, False, False)
            self.custom_assert_method_stub(Extinf, 'meth2', 0, True, False)
            self.custom_assert_method_stub(Extinf, 'meth4', 2, False, False)
            self.custom_assert_method_stub(Extinf, 'meth5', 1, True, False)
            self.custom_assert_method_stub(Extinf, 'meth6', 1, False, True)
            self.custom_assert_method_stub(Extinf, 'meth7', 3, True, True)

        with self.subTest(extending='ITestInterface3'):
            Extinf = ITestInterface1.extended(ITestInterface3)
            self.assertIsInstance(Extinf, Interface)
            self.assertEqual(Extinf.__name__, 'ITestInterface3')
            self.custom_assert_method_stub(Extinf, 'meth1', 0, False, False)
            self.custom_assert_method_stub(Extinf, 'meth3', 0, False, True)
            self.custom_assert_method_stub(Extinf, 'meth4', 2, False, False)
            self.custom_assert_method_stub(Extinf, 'meth5', 1, True, False)
            self.custom_assert_method_stub(Extinf, 'meth6', 1, False, True)
            self.custom_assert_method_stub(Extinf, 'meth7', 3, True, True)

    def test_implemented(self):
        """
        Tests implemented method
        """
        self.assertTrue(ITestInterface1.implemented(TestClass))
        self.assertFalse(ITestInterface2.implemented(TestClass))
        self.assertFalse(ITestInterface3.implemented(TestClass))

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
        self.assertRaises(Exception, lambda: ITestInterface2(TestClass))
        self.assertRaises(Exception, lambda: ITestInterface3(TestClass))

    def test_call_for_assert_instance_error(self):
        """
        Tests erroring instance assertion __call__
        """
        test_inst = TestClass()
        self.assertRaises(Exception, lambda: ITestInterface2(test_inst))
        self.assertRaises(Exception, lambda: ITestInterface3(test_inst))

    def test_call_for_extend(self):
        """
        Tests extension __call__
        """
        with self.subTest(extending='ITestInterface2'):
            Extinf = ITestInterface1(ITestInterface2)
            self.assertIsInstance(Extinf, Interface)
            self.assertEqual(Extinf.__name__, 'ITestInterface2')
            self.custom_assert_method_stub(Extinf, 'meth1', 0, False, False)
            self.custom_assert_method_stub(Extinf, 'meth2', 0, True, False)
            self.custom_assert_method_stub(Extinf, 'meth4', 2, False, False)
            self.custom_assert_method_stub(Extinf, 'meth5', 1, True, False)
            self.custom_assert_method_stub(Extinf, 'meth6', 1, False, True)
            self.custom_assert_method_stub(Extinf, 'meth7', 3, True, True)

        with self.subTest(extending='ITestInterface3'):
            Extinf = ITestInterface1(ITestInterface3)
            self.assertIsInstance(Extinf, Interface)
            self.assertEqual(Extinf.__name__, 'ITestInterface3')
            self.custom_assert_method_stub(Extinf, 'meth1', 0, False, False)
            self.custom_assert_method_stub(Extinf, 'meth3', 0, False, True)
            self.custom_assert_method_stub(Extinf, 'meth4', 2, False, False)
            self.custom_assert_method_stub(Extinf, 'meth5', 1, True, False)
            self.custom_assert_method_stub(Extinf, 'meth6', 1, False, True)
            self.custom_assert_method_stub(Extinf, 'meth7', 3, True, True)