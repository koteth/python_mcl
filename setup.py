#!/usr/bin/env python

from distutils.core import setup

setup(
    name='MCL_Markov_Cluster',
    version='0.3',
    description='Markov Cluster algorithm implementation',
    url = 'https://github.com/koteth/python_mcl',
    scripts = [
        'mcl/mcl_clustering.py'
    ],
    install_requires = ['numpy', 'networkx'],
    keywords = "MCL markov clustering graph",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    author='Gabriele Lami',
    packages=['mcl'],
)
