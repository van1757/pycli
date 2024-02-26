from setuptools import find_packages, setup

__version__ = "0.0.1"
__description__ = "Python-written clone of Unix commands"

setup(
    name="pycli_learning",
    version=__version__,
    author="Alexey Radkevich",
    description=__description__,
    packages=find_packages(),
    keywords=["python"],
)
