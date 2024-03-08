# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rotten_tomatoes_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    LISTS_JSON = "/lists.json"
    LISTS_DVDS_JSON = "/lists/dvds.json"
    LISTS_DVDS_CURRENT_RELEASES_JSON = "/lists/dvds/current_releases.json"
    LISTS_DVDS_NEW_RELEASES_JSON = "/lists/dvds/new_releases.json"
    LISTS_DVDS_TOP_RENTALS_JSON = "/lists/dvds/top_rentals.json"
    LISTS_DVDS_UPCOMING_JSON = "/lists/dvds/upcoming.json"
    LISTS_MOVIES_JSON = "/lists/movies.json"
    LISTS_MOVIES_BOX_OFFICE_JSON = "/lists/movies/box_office.json"
    LISTS_MOVIES_IN_THEATERS_JSON = "/lists/movies/in_theaters.json"
    LISTS_MOVIES_OPENING_JSON = "/lists/movies/opening.json"
    LISTS_MOVIES_UPCOMING_JSON = "/lists/movies/upcoming.json"
    MOVIE_ALIAS_JSON = "/movie_alias.json"
    MOVIES_JSON = "/movies.json"
    MOVIES_ID_JSON = "/movies/{id}.json"
    MOVIES_ID_CAST_JSON = "/movies/{id}/cast.json"
    MOVIES_ID_CLIPS_JSON = "/movies/{id}/clips.json"
    MOVIES_ID_REVIEWS_JSON = "/movies/{id}/reviews.json"
    MOVIES_ID_SIMILAR_JSON = "/movies/{id}/similar.json"
