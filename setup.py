from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name="kct_pygame_utils",
    version="1.0.1",
    description="A simple python library that provides utilities for pygame games",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="https://github.com/KidCoderT/my_first_package",
    authors="KidCoderT",
    author_email="tejas75o25@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="",
    packages=find_packages(),
    install_requires=["pygame"],
)
