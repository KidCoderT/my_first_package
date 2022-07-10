from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

long_description = """
# KCT Pygame Utils

A set of handy pygame functions and classes to help with in making you next new game.

features include

1. Contains Utils that can handle image scaling, opacity, outline and sprite sheets
2. Contains Classes that can be extended to create Particle Systems
3. Contains methods to easily make a scrolling background
4. Contains methods that can help with text

This is my very first module built with the python for geeks book.

If you want references on how to use this module go to the [examples folder](https://github.com/KidCoderT/my_first_package/tree/master/kct_pygame_utils/examples) and here it contains 5 different tests each showing a use case of one or more of the function and methods provided by the package.


Change Log                @KCT
==============================

0.0.1 (10/07/2020)
-------------------
- Initial release
"""

setup(
    name="kctpygameutils",
    version="1.0.1",
    description="A simple python library that provides utilities for pygame games",
    long_description=long_description,
    url="https://github.com/KidCoderT/my_first_package",
    authors="KidCoderT",
    author_email="tejas75o25@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="",
    packages=find_packages(),
    install_requires=["pygame"],
)
