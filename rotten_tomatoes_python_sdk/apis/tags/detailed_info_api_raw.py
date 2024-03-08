# coding: utf-8

"""
    Rotten Tomatoes

    Test our API services using I/O Docs.

    The version of the OpenAPI document: 1.0
    Contact: mike.ralphson@gmail.com
    Created by: https://github.com/mermade/mashery2openapi
"""

from rotten_tomatoes_python_sdk.paths.movies_id_similar_json.get import FindSimilarMoviesRaw
from rotten_tomatoes_python_sdk.paths.movies_id_clips_json.get import GetClipByIdRaw
from rotten_tomatoes_python_sdk.paths.movie_alias_json.get import GetMovieAliasInfoRaw
from rotten_tomatoes_python_sdk.paths.movies_id_json.get import GetMovieByIdJsonRaw
from rotten_tomatoes_python_sdk.paths.movies_id_cast_json.get import GetMovieCastRaw
from rotten_tomatoes_python_sdk.paths.movies_id_reviews_json.get import GetMovieReviewsRaw


class DetailedInfoApiRaw(
    FindSimilarMoviesRaw,
    GetClipByIdRaw,
    GetMovieAliasInfoRaw,
    GetMovieByIdJsonRaw,
    GetMovieCastRaw,
    GetMovieReviewsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass