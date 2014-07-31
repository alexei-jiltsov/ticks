#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ticks',
    version='0.0.1',
    packages = find_packages(),
    url='',
    license='',
    author='Eric Nelson',
    author_email='gauntletguy2@gmail.com',
    description='',
    entry_points = {
      'console_scripts': [
        'ticks = ticks:main',
        'idle = idlelib.PyShell:main'
      ]
    }
)
