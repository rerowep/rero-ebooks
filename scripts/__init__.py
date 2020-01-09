#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# This file is part of RERO Ebooks.
# Copyright (C) 2018 RERO.
#
# RERO Ebooks is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# RERO Ebooks is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RERO Ebooks; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Poetry script utils."""

import os
# import subprocess
import sys

# def __getattr__(name):  # python 3.7+, otherwise define each script manually
#     name = name.replace('_', '-')
#     subprocess.run(
#         ['python', '-u', '-m', name] + sys.argv[1:]
#     )  # run whatever you like based on 'name'


def run(prg_name):  # python 3.7+, otherwise define each script manually
    def fn():
        # Replace current Python program by prg_name (same PID)
        os.execvp(prg_name, [prg_name] + sys.argv[1:])
    return fn