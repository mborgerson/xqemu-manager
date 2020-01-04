#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="XQEMU-Manager",
    version="0-dev",
    maintainer="XQEMU maintainers",
    description="Simple graphical user interface to manage XQEMU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xqemu/xqemu-manager",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: System :: Emulators",
    ),
    install_requires=['PyQt5'],
    packages=['xqemu-manager'],
    package_dir={'xqemu-manager': ''},
    package_data={'xqemu-manager': ['*.ui']},
)
