import typing_extensions

from rotten_tomatoes_python_sdk.apis.tags import TagValues
from rotten_tomatoes_python_sdk.apis.tags.detailed_info_api import DetailedInfoApi
from rotten_tomatoes_python_sdk.apis.tags.movie_lists_api import MovieListsApi
from rotten_tomatoes_python_sdk.apis.tags.dvd_lists_api import DVDListsApi
from rotten_tomatoes_python_sdk.apis.tags.top_level_lists_api import TopLevelListsApi
from rotten_tomatoes_python_sdk.apis.tags.search_api import SearchApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DETAILED_INFO: DetailedInfoApi,
        TagValues.MOVIE_LISTS: MovieListsApi,
        TagValues.DVD_LISTS: DVDListsApi,
        TagValues.TOP_LEVEL_LISTS: TopLevelListsApi,
        TagValues.SEARCH: SearchApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DETAILED_INFO: DetailedInfoApi,
        TagValues.MOVIE_LISTS: MovieListsApi,
        TagValues.DVD_LISTS: DVDListsApi,
        TagValues.TOP_LEVEL_LISTS: TopLevelListsApi,
        TagValues.SEARCH: SearchApi,
    }
)
