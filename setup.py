#!/usr/bin/env python
"""
A simple Python class for easier name matching (especially in academia)
Project website: https://github.com/yymao/fuzzyname
The MIT License (MIT)
Copyright (c) 2018 Yao-Yuan Mao (yymao)
http://opensource.org/licenses/MIT
"""

from setuptools import setup

setup(
    name='fuzzyname',
    version='0.1.0',
    description='A simple Python class for easier name matching (especially in academia).',
    url='https://github.com/yymao/fuzzyname',
    download_url = 'https://github.com/yymao/fuzzyname/archive/v0.1.0.zip',
    author='Yao-Yuan Mao',
    author_email='yymao.astro@gmail.com',
    maintainer='Yao-Yuan Mao',
    maintainer_email='yymao.astro@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='fuzzyname',
    py_modules=['fuzzyname'],
)
