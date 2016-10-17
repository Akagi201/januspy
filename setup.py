#! /usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
import re
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

try:
    import pypandoc

    here = os.path.abspath(os.path.dirname(__file__))
    ld = pypandoc.convert(os.path.join(here, 'README.md'), 'rst')
except(IOError, ImportError):
    ld = 'See:\nhttps://github.com/Akagi201/januspy\n'

setup(
    name='januspy',
    version=find_version('januspy', 'janus.py'),
    license='License :: OSI Approved :: MIT License',
    platforms='Platform Independent',
    author='Akagi201',
    author_email='akagi201@gmail.com',
    packages=['januspy', ],
    url='https://github.com/Akagi201/januspy',
    description='Elegant python client to interact with Janus Gateway.',
    long_description=ld,
    keywords=['janus', 'webrtc'],
    install_requires=['requests>=2.4.3'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
