import typing_extensions

from rotten_tomatoes_python_sdk.paths import PathValues
from rotten_tomatoes_python_sdk.apis.paths.lists_json import ListsJson
from rotten_tomatoes_python_sdk.apis.paths.lists_dvds_json import ListsDvdsJson
from rotten_tomatoes_python_sdk.apis.paths.lists_dvds_current_releases_json import ListsDvdsCurrentReleasesJson
from rotten_tomatoes_python_sdk.apis.paths.lists_dvds_new_releases_json import ListsDvdsNewReleasesJson
from rotten_tomatoes_python_sdk.apis.paths.lists_dvds_top_rentals_json import ListsDvdsTopRentalsJson
from rotten_tomatoes_python_sdk.apis.paths.lists_dvds_upcoming_json import ListsDvdsUpcomingJson
from rotten_tomatoes_python_sdk.apis.paths.lists_movies_json import ListsMoviesJson
from rotten_tomatoes_python_sdk.apis.paths.lists_movies_box_office_json import ListsMoviesBoxOfficeJson
from rotten_tomatoes_python_sdk.apis.paths.lists_movies_in_theaters_json import ListsMoviesInTheatersJson
from rotten_tomatoes_python_sdk.apis.paths.lists_movies_opening_json import ListsMoviesOpeningJson
from rotten_tomatoes_python_sdk.apis.paths.lists_movies_upcoming_json import ListsMoviesUpcomingJson
from rotten_tomatoes_python_sdk.apis.paths.movie_alias_json import MovieAliasJson
from rotten_tomatoes_python_sdk.apis.paths.movies_json import MoviesJson
from rotten_tomatoes_python_sdk.apis.paths.movies_id_json import MoviesIdJson
from rotten_tomatoes_python_sdk.apis.paths.movies_id_cast_json import MoviesIdCastJson
from rotten_tomatoes_python_sdk.apis.paths.movies_id_clips_json import MoviesIdClipsJson
from rotten_tomatoes_python_sdk.apis.paths.movies_id_reviews_json import MoviesIdReviewsJson
from rotten_tomatoes_python_sdk.apis.paths.movies_id_similar_json import MoviesIdSimilarJson

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.LISTS_JSON: ListsJson,
        PathValues.LISTS_DVDS_JSON: ListsDvdsJson,
        PathValues.LISTS_DVDS_CURRENT_RELEASES_JSON: ListsDvdsCurrentReleasesJson,
        PathValues.LISTS_DVDS_NEW_RELEASES_JSON: ListsDvdsNewReleasesJson,
        PathValues.LISTS_DVDS_TOP_RENTALS_JSON: ListsDvdsTopRentalsJson,
        PathValues.LISTS_DVDS_UPCOMING_JSON: ListsDvdsUpcomingJson,
        PathValues.LISTS_MOVIES_JSON: ListsMoviesJson,
        PathValues.LISTS_MOVIES_BOX_OFFICE_JSON: ListsMoviesBoxOfficeJson,
        PathValues.LISTS_MOVIES_IN_THEATERS_JSON: ListsMoviesInTheatersJson,
        PathValues.LISTS_MOVIES_OPENING_JSON: ListsMoviesOpeningJson,
        PathValues.LISTS_MOVIES_UPCOMING_JSON: ListsMoviesUpcomingJson,
        PathValues.MOVIE_ALIAS_JSON: MovieAliasJson,
        PathValues.MOVIES_JSON: MoviesJson,
        PathValues.MOVIES_ID_JSON: MoviesIdJson,
        PathValues.MOVIES_ID_CAST_JSON: MoviesIdCastJson,
        PathValues.MOVIES_ID_CLIPS_JSON: MoviesIdClipsJson,
        PathValues.MOVIES_ID_REVIEWS_JSON: MoviesIdReviewsJson,
        PathValues.MOVIES_ID_SIMILAR_JSON: MoviesIdSimilarJson,
    }
)

path_to_api = PathToApi(
    {
        PathValues.LISTS_JSON: ListsJson,
        PathValues.LISTS_DVDS_JSON: ListsDvdsJson,
        PathValues.LISTS_DVDS_CURRENT_RELEASES_JSON: ListsDvdsCurrentReleasesJson,
        PathValues.LISTS_DVDS_NEW_RELEASES_JSON: ListsDvdsNewReleasesJson,
        PathValues.LISTS_DVDS_TOP_RENTALS_JSON: ListsDvdsTopRentalsJson,
        PathValues.LISTS_DVDS_UPCOMING_JSON: ListsDvdsUpcomingJson,
        PathValues.LISTS_MOVIES_JSON: ListsMoviesJson,
        PathValues.LISTS_MOVIES_BOX_OFFICE_JSON: ListsMoviesBoxOfficeJson,
        PathValues.LISTS_MOVIES_IN_THEATERS_JSON: ListsMoviesInTheatersJson,
        PathValues.LISTS_MOVIES_OPENING_JSON: ListsMoviesOpeningJson,
        PathValues.LISTS_MOVIES_UPCOMING_JSON: ListsMoviesUpcomingJson,
        PathValues.MOVIE_ALIAS_JSON: MovieAliasJson,
        PathValues.MOVIES_JSON: MoviesJson,
        PathValues.MOVIES_ID_JSON: MoviesIdJson,
        PathValues.MOVIES_ID_CAST_JSON: MoviesIdCastJson,
        PathValues.MOVIES_ID_CLIPS_JSON: MoviesIdClipsJson,
        PathValues.MOVIES_ID_REVIEWS_JSON: MoviesIdReviewsJson,
        PathValues.MOVIES_ID_SIMILAR_JSON: MoviesIdSimilarJson,
    }
)
