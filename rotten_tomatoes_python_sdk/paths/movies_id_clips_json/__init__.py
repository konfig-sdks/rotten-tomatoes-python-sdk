# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rotten_tomatoes_python_sdk.paths.movies_id_clips_json import Api

from rotten_tomatoes_python_sdk.paths import PathValues

path = PathValues.MOVIES_ID_CLIPS_JSON