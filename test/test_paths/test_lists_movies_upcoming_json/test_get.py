# coding: utf-8

"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

import unittest
from unittest.mock import patch

import urllib3

import rotten_tomatoes_python_sdk
from rotten_tomatoes_python_sdk.paths.lists_movies_upcoming_json import get
from rotten_tomatoes_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestListsMoviesUpcomingJson(ApiTestMixin, unittest.TestCase):
    """
    ListsMoviesUpcomingJson unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
