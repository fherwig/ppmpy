from setuptools import setup, find_packages

setup(
    name = "ppmpy",
    version = "0.1",
    packages = find_packages(),
    install_requires = ["numpy", "setuptools","nugridpy"],
    author = "Falk Herwig, Sam Jones, Robert Andrassy, Daniel Alexander Bertolino Conti ",
    author_email = "fherwig@uvic.ca")
