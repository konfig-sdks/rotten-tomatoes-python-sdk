# coding: utf-8

# flake8: noqa

"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

__version__ = "1.0"

# import ApiClient
from rotten_tomatoes_python_sdk.api_client import ApiClient

# import Configuration
from rotten_tomatoes_python_sdk.configuration import Configuration

# import exceptions
from rotten_tomatoes_python_sdk.exceptions import OpenApiException
from rotten_tomatoes_python_sdk.exceptions import ApiAttributeError
from rotten_tomatoes_python_sdk.exceptions import ApiTypeError
from rotten_tomatoes_python_sdk.exceptions import ApiValueError
from rotten_tomatoes_python_sdk.exceptions import ApiKeyError
from rotten_tomatoes_python_sdk.exceptions import ApiException

from rotten_tomatoes_python_sdk.client import RottenTomatoes
