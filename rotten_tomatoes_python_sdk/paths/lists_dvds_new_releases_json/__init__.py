# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rotten_tomatoes_python_sdk.paths.lists_dvds_new_releases_json import Api

from rotten_tomatoes_python_sdk.paths import PathValues

path = PathValues.LISTS_DVDS_NEW_RELEASES_JSON