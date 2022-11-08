#!/usr/bin/python
from os.path import isfile
import codecs
import os
import re

from setuptools import setup


if isfile("MANIFEST"):
    os.unlink("MANIFEST")


TOPDIR = os.path.dirname(__file__) or "."
VERSION = re.search('__version__ = "([^"]+)"',
                    codecs.open(TOPDIR + "/europarse/__init__.py",
                                encoding='utf-8').read()).group(1)


setup(name="europarse",
    version=VERSION,
    description="dateutil.parser, but not broken",
    author="Matt Westcott",
    author_email="matt@west.co.tt",
    url="https://github.com/demozoo/europarse",
    license="Simplified BSD",
    long_description="""
A fork of dateutil.parser from before it broke the semantics of the
'dayfirst' argument to treat ISO dates as YYYY-DD-MM.
""",
    packages=["europarse", "europarse.zoneinfo", "europarse.tz"],
    package_data={"europarse.zoneinfo": ["europarse-zoneinfo.tar.gz"]},
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite="europarse.test",
    python_requires=">=3.7",
)
