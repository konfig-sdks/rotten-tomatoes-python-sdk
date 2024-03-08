# coding: utf-8
"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

import typing
import inspect
from datetime import date, datetime
from rotten_tomatoes_python_sdk.client_custom import ClientCustom
from rotten_tomatoes_python_sdk.configuration import Configuration
from rotten_tomatoes_python_sdk.api_client import ApiClient
from rotten_tomatoes_python_sdk.type_util import copy_signature
from rotten_tomatoes_python_sdk.apis.tags.dvd_lists_api import DVDListsApi
from rotten_tomatoes_python_sdk.apis.tags.detailed_info_api import DetailedInfoApi
from rotten_tomatoes_python_sdk.apis.tags.movie_lists_api import MovieListsApi
from rotten_tomatoes_python_sdk.apis.tags.search_api import SearchApi
from rotten_tomatoes_python_sdk.apis.tags.top_level_lists_api import TopLevelListsApi



class RottenTomatoes(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.dvd_lists: DVDListsApi = DVDListsApi(api_client)
        self.detailed_info: DetailedInfoApi = DetailedInfoApi(api_client)
        self.movie_lists: MovieListsApi = MovieListsApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.top_level_lists: TopLevelListsApi = TopLevelListsApi(api_client)
