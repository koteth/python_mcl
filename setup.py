#!/usr/bin/env python

from distutils.core import setup

setup(
    name='MCL Markov Cluster',
    version='0.3',
    description='Markov Cluster algorithm implementation',
    scripts = [
        'mcl/mcl_clustering.py'
    ],
    install_requires = ['numpy', 'networkx'],
    keywords = "MCL markov clustering graph",
    author='Gabriele Lami',
    packages=['mcl'],
)
