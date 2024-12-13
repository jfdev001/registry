"""Setup python project.

References:
    [1] : https://xebia.com/blog/a-practical-guide-to-using-setup-py/
"""
from setuptools import find_packages, setup


setup(
    name="registry",
    packages=find_packages(include=["mod"]),
    version='0.1.0',
)
