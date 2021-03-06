# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
# this contains imports plugins that configure py.test for asdf tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.

import os

import pytest

from .extern.RangeHTTPServer import RangeHTTPRequestHandler

# This is to figure out the affiliated package version, rather than
# using Astropy's
from . import version
from .tests.httpserver import HTTPServer, RangeHTTPServer


@pytest.fixture()
def httpserver(request):
    """
    The returned ``httpserver`` provides a threaded HTTP server
    instance.  It serves content from a temporary directory (available
    as the attribute tmpdir) at randomly assigned URL (available as
    the attribute url).

    * ``tmpdir`` - path to the tmpdir that it's serving from (str)
    * ``url`` - the base url for the server
    """
    server = HTTPServer()
    request.addfinalizer(server.finalize)
    return server


@pytest.fixture()
def rhttpserver(request):
    """
    The returned ``httpserver`` provides a threaded HTTP server
    instance.  It serves content from a temporary directory (available
    as the attribute tmpdir) at randomly assigned URL (available as
    the attribute url).  The server supports HTTP Range headers.

    * ``tmpdir`` - path to the tmpdir that it's serving from (str)
    * ``url`` - the base url for the server
    """
    server = RangeHTTPServer()
    request.addfinalizer(server.finalize)
    return server
