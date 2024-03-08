# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rotten_tomatoes_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DETAILED_INFO = "Detailed Info"
    MOVIE_LISTS = "Movie Lists"
    DVD_LISTS = "DVD Lists"
    TOP_LEVEL_LISTS = "Top Level Lists"
    SEARCH = "Search"
