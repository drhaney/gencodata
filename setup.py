##############################################################################
#
# Copyright (c) 2017 Gronk Bogotronix
# All Rights Reserved.
#
# This software is subject to the restrictions of the BSD 2-Clause or
# Simplified BSD license as stated at:
# https://opensource.org/licenses/BSD-2-Clause
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1.  Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2.  Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
#
##############################################################################

import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.txt')).read()
except:
    README = ''

requires = []

setup(
    name='gencodata',
    version='0.2',
    description=('CODATA physical constants file generator'),
    long_description=README + '\n\n',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        ],
    keywords='CODATA physical constants file generator',
    author="Proontny Platterpoont",
    author_email="pp@urology.net",
    url="localhost",
    license="BSD 2-Clause",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '':['json','*.txt','*.inp','*.html','*.md','*.rst'],
        'gencodata':['json','*.txt','*.inp','*.html','*.md','*.rst'],
        'gencodata/examples':['*.txt','*.inp'],
        'gencodata/test':['json','*.txt','*.inp'],
        'doc':['*.rst','*.html']
        },
    zip_safe=False,
    tests_require = requires,
    install_requires = requires,
    test_suite=None,
    scripts = ['bin/gencodata']
    )

