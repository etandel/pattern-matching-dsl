from setuptools import setup, find_packages
from pattern import __version__


setup(
    name='pattern',
    version=__version__,
    description='Library for string pattern matching.',
    packages=find_packages(),
)

