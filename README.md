# Good Interface

Provides the Interface class and other utilities which can define method "interfaces" which automatically check method implementation in classes and objects.

## Interfaces

An Interface is a collection of methods that are to be implemented in classes that implement this Interface. The Interface class can define Interfaces from a class skeleton.

```python
from good.interface import Interface

@Interface
class MyInterface:
    def method1(self, arg1, arg2):
        pass

    def method2(self, arg2):
        pass
```

Since the interface is callable, you can call the new Interface object as a decorator on a class, which provides a check on the given class, ensuring that it implements the defined methods in the given interface.

```python
from good.interface import Interface

@Interface
class MyInterface:
    def method1(self, arg1, arg2):
        pass

    def method2(self, arg2):
        pass

@MyInterface
class MyClass:
    def method1(self, arg1, arg2):
        pass

    def method2(self, arg2):
        pass
```

Calling the interface on another interface will extends the interface, adding the methods of this current interface to the new interface

```python
from good.interface import Interface

@Interface
class MyInterface1:
    def method1(self):
        pass

@MyInterface1
@Interface
class MyInterface2:
    def method2(self, arg1, arg2):
        pass

    def method3(self, arg2):
        pass

# Creates:
#
# @Interface
# class MyInterface2:
#     def method1(self):
#         pass
#
#     def method2(self, arg1, arg2):
#         pass
#
#     def method3(self, arg2):
#         pass
```