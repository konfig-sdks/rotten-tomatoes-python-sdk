# coding: utf-8
"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

import typing

from rotten_tomatoes_python_sdk.configuration import Configuration
from rotten_tomatoes_python_sdk.api_client import ApiClient



class ClientCustom:

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        # customize here

    # add custom methods here