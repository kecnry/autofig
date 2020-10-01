#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='autofig',
      version='1.2.0',
      description='High-Level Interface to Create Figures/Animations with Matplotlib',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Kyle Conroy',
      author_email='kyleconroy@gmail.com',
      url='https://www.github.com/kecnry/autofig',
      download_url = 'https://github.com/kecnry/autofig/tarball/1.1.0',
      packages=['autofig'],
     scripts=['launcher/autofig'],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
       ],
     )
