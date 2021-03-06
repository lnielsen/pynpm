# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Pytest configuration."""

from __future__ import absolute_import, print_function

import json
import shutil
import tempfile
from os.path import dirname, join

import pkg_resources
import pytest


@pytest.yield_fixture()
def tmpdir():
    """Temporary directory."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


@pytest.fixture()
def pkgdir_source():
    """Get source of package directory tests/jspkg/."""
    return join(dirname(__file__), 'jspkg')


@pytest.fixture()
def pkg(pkgdir_source, tmpdir):
    """Initialize package directory content."""
    pkgdir = join(tmpdir, 'jspkg')
    shutil.copytree(pkgdir_source, pkgdir)
    return join(pkgdir, 'package.json')


@pytest.fixture()
def deppkg(tmpdir):
    """Initialize package directory content."""
    src = join(dirname(__file__), 'jsdep')
    dst = join(tmpdir, 'jsdep')
    shutil.copytree(src, dst)
    return join(dst, 'package.json')


@pytest.fixture()
def pkgjson_source(pkgdir_source):
    """Initialize package directory content."""
    with open(join(pkgdir_source, 'package.json'), 'r') as fp:
        return json.load(fp)
