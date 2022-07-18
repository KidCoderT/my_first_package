from setuptools import setup

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name="kct_pygame_tools",
    version="2.0.3",
    author="KidCoderT",
    author_email="tejas75o25@gmail.com",
    packages=["kct_pygame_tools", "kct_pygame_tools/ui"],
    python_requires=">=3.5, <4",
    url="https://test.pypi.org/project/kct-pygame-tools/",
    license="LICENSE.txt",
    description="A simple python library that provides utilities for pygame games",
    long_description=open("README.md").read(),
    install_requires=["pygame", "pillow"],
    classifiers=classifiers,
)
