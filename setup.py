#!/usr/bin/env python

from distutils.core import setup

setup(
    name='MCL Markov Clustering',
    version='0.3',
    description='Markov Clustering algoritm for Graphs',
    scripts = [
        'mcl/mcl_clustering.py'
    ],
    author='koteth',
    install_requires = ['numpy', 'networkx'],
    keywords = "MCL markov clustering graph",
    author='Gabriele Lami',
    packages=['mcl'],
)
