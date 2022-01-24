#!/usr/bin/env python
"""
A simple Python class for easier name matching (especially in academia)
Project website: https://github.com/yymao/fuzzyname
The MIT License (MIT)
Copyright (c) 2018-2022 Yao-Yuan Mao (yymao)
http://opensource.org/licenses/MIT
"""

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "fuzzyname", "version.py")) as f:
    exec(f.read())  # pylint: disable=W0122

setup(
    name="fuzzyname",
    version=__version__,  # pylint: disable=E0602 # noqa: F821
    description="A simple Python class for easier name matching (especially in academia).",
    url="https://github.com/yymao/fuzzyname",
    download_url="https://github.com/yymao/fuzzyname/archive/{}.zip".format(
        __version__  # pylint: disable=E0602 # noqa: F821
    ),
    author="Yao-Yuan Mao",
    author_email="yymao.astro@gmail.com",
    maintainer="Yao-Yuan Mao",
    maintainer_email="yymao.astro@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="fuzzyname",
    packages=find_packages(),
    install_requires=["Unidecode"],
)
