# coding: utf-8

"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

import unittest

import os
from pprint import pprint
from rotten_tomatoes_python_sdk import RottenTomatoes

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        rottentomatoes = RottenTomatoes(
        
                        key = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(rottentomatoes)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
