"""
Good Interface

Provides the Interface class and other utilities
which can define method "interfaces" which
automatically check method implementation in
classes and objects.

Author:  Anshul Kharbanda
Created: 6 - 26 - 2018
"""
from setuptools import setup

# Long description
with open('README.md', 'r') as file:
    long_description = file.read()

# Create setup function
setup(name='good-interface',
      version='1.0.1',
      description='Provides the Interface class and other interface utilities.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Anshul Kharbanda',
      author_email='akanshul97@gmail.com',
      url='https://www.github.org/andydevs/good-handlers',
      packages=['good_interface'])
