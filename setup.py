"""
Copyright 2014 Jason Heeris, jason.heeris@gmail.com
Copyright 2012 Leif Johnson, leif@leifjohnson.net

This file is part of async-nethack.

`async-nethack` is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

`async-nethack` is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
`async-nethack`. If not, see <http://www.gnu.org/licenses/>.
"""

import os
import setuptools

setuptools.setup(
    name = 'asyncnethack',
    version = '1',
    packages = setuptools.find_packages(),

    author = 'Jason Heeris',
    author_email = 'jason.heeris@gmail.com',
    description = 'An asynchronous interface to nethack',

    license = 'GPL-3',

    url = 'http://github.com/detly/py-nethack',

    keywords = ('nethack',),

    entry_points = {
        'console_scripts': [
            'asyncnethack = asyncnethack.console:main',
        ]
    }
)
