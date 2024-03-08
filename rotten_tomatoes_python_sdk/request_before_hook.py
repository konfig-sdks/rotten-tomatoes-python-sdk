# coding: utf-8

"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

import typing
from urllib3._collections import HTTPHeaderDict
from rotten_tomatoes_python_sdk.configuration import Configuration

def request_before_hook(
        resource_path: str,
        method: str,
        configuration: Configuration,
        path_template: str,
        headers: typing.Optional[HTTPHeaderDict] = None,
        body: typing.Any = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any
):
    pass