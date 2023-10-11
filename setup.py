from setuptools import setup
from setuptools import find_packages

long_description= """
Text analysis tools for the Computers and the Humanities Course
"""

required = [
    "pandas",
    "statistics",
    "networkx",
]

setup(
    name="networkprocessing",
    version="0.0.1",
    description="Network processing tools",
    long_description=long_description,
    author="Miguel Escobar Varela",
    install_requires=required,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
)
