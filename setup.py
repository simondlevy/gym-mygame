'''
Python distutils setup file for gym-mygame module.

Copyright (C) 2020 Simon D. Levy

MIT License
'''

#from distutils.core import setup
from setuptools import setup

setup (name = 'gym_mygame',
    version = '0.1',
    install_requires = ['gym', 'numpy'],
    description = 'Gym environment for my CSCI 316 game',
    packages = ['gym_mygame', 'gym_mygame.envs'],
    author='Simon D. Levy',
    author_email='simon.d.levy@gmail.com',
    url='https://github.com/simondlevy/studenta21/gym-mygame',
    license='MIT',
    platforms='Linux; Windows; OS X'
    )
