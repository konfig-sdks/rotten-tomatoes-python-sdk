# coding: utf-8

"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

from rotten_tomatoes_python_sdk.paths.movies_id_similar_json.get import FindSimilarMovies
from rotten_tomatoes_python_sdk.paths.movies_id_clips_json.get import GetClipById
from rotten_tomatoes_python_sdk.paths.movie_alias_json.get import GetMovieAliasInfo
from rotten_tomatoes_python_sdk.paths.movies_id_json.get import GetMovieByIdJson
from rotten_tomatoes_python_sdk.paths.movies_id_cast_json.get import GetMovieCast
from rotten_tomatoes_python_sdk.paths.movies_id_reviews_json.get import GetMovieReviews
from rotten_tomatoes_python_sdk.apis.tags.detailed_info_api_raw import DetailedInfoApiRaw


class DetailedInfoApi(
    FindSimilarMovies,
    GetClipById,
    GetMovieAliasInfo,
    GetMovieByIdJson,
    GetMovieCast,
    GetMovieReviews,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DetailedInfoApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DetailedInfoApiRaw(api_client)