<div align="center">

[![Visit Rotten tomatoes](./header.png)](https://developer.fandango.com&#x2F;rotten_tomatoes)

# Rotten tomatoes<a id="rotten-tomatoes"></a>

Test our API services using I/O Docs.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`rottentomatoes.dvd_lists.get_current_releases`](#rottentomatoesdvd_listsget_current_releases)
  * [`rottentomatoes.dvd_lists.get_new_releases_json`](#rottentomatoesdvd_listsget_new_releases_json)
  * [`rottentomatoes.dvd_lists.get_top_rentals_json`](#rottentomatoesdvd_listsget_top_rentals_json)
  * [`rottentomatoes.dvd_lists.get_upcoming_dvds`](#rottentomatoesdvd_listsget_upcoming_dvds)
  * [`rottentomatoes.detailed_info.find_similar_movies`](#rottentomatoesdetailed_infofind_similar_movies)
  * [`rottentomatoes.detailed_info.get_clip_by_id`](#rottentomatoesdetailed_infoget_clip_by_id)
  * [`rottentomatoes.detailed_info.get_movie_alias_info`](#rottentomatoesdetailed_infoget_movie_alias_info)
  * [`rottentomatoes.detailed_info.get_movie_by_id_json`](#rottentomatoesdetailed_infoget_movie_by_id_json)
  * [`rottentomatoes.detailed_info.get_movie_cast`](#rottentomatoesdetailed_infoget_movie_cast)
  * [`rottentomatoes.detailed_info.get_movie_reviews`](#rottentomatoesdetailed_infoget_movie_reviews)
  * [`rottentomatoes.movie_lists.get_box_office_json`](#rottentomatoesmovie_listsget_box_office_json)
  * [`rottentomatoes.movie_lists.get_intheater_movies`](#rottentomatoesmovie_listsget_intheater_movies)
  * [`rottentomatoes.movie_lists.get_opening_movies`](#rottentomatoesmovie_listsget_opening_movies)
  * [`rottentomatoes.movie_lists.get_upcoming_movies`](#rottentomatoesmovie_listsget_upcoming_movies)
  * [`rottentomatoes.search.movies_json`](#rottentomatoessearchmovies_json)
  * [`rottentomatoes.top_level_lists.get_data`](#rottentomatoestop_level_listsget_data)
  * [`rottentomatoes.top_level_lists.get_dvds`](#rottentomatoestop_level_listsget_dvds)
  * [`rottentomatoes.top_level_lists.get_movies_json`](#rottentomatoestop_level_listsget_movies_json)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Rotten%20Tomatoes&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from rotten_tomatoes_python_sdk import RottenTomatoes, ApiException

rottentomatoes = RottenTomatoes(
    key="YOUR_API_KEY",
)

try:
    rottentomatoes.dvd_lists.get_current_releases(
        page_limit="16",
        page="1",
        country="us",
    )
except ApiException as e:
    print("Exception when calling DVDListsApi.get_current_releases: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from rotten_tomatoes_python_sdk import RottenTomatoes, ApiException

rottentomatoes = RottenTomatoes(
    key="YOUR_API_KEY",
)


async def main():
    try:
        await rottentomatoes.dvd_lists.aget_current_releases(
            page_limit="16",
            page="1",
            country="us",
        )
    except ApiException as e:
        print("Exception when calling DVDListsApi.get_current_releases: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from rotten_tomatoes_python_sdk import RottenTomatoes, ApiException

rottentomatoes = RottenTomatoes(
    key="YOUR_API_KEY",
)

try:
    get_current_releases_response = rottentomatoes.dvd_lists.raw.get_current_releases(
        page_limit="16",
        page="1",
        country="us",
    )
    pprint(get_current_releases_response.headers)
    pprint(get_current_releases_response.status)
    pprint(get_current_releases_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DVDListsApi.get_current_releases: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `rottentomatoes.dvd_lists.get_current_releases`<a id="rottentomatoesdvd_listsget_current_releases"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.dvd_lists.get_current_releases(
    page_limit="16",
    page="1",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_limit: `str`<a id="page_limit-str"></a>

The amount of new release dvds to show per page

##### page: `str`<a id="page-str"></a>

The selected page of current DVD releases

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/dvds/current_releases.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.dvd_lists.get_new_releases_json`<a id="rottentomatoesdvd_listsget_new_releases_json"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.dvd_lists.get_new_releases_json(
    page_limit="16",
    page="1",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_limit: `str`<a id="page_limit-str"></a>

The amount of new release dvds to show per page

##### page: `str`<a id="page-str"></a>

The selected page of new release DVDs

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/dvds/new_releases.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.dvd_lists.get_top_rentals_json`<a id="rottentomatoesdvd_listsget_top_rentals_json"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.dvd_lists.get_top_rentals_json(
    limit="10",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

Limits the number of top rentals returned

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/dvds/top_rentals.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.dvd_lists.get_upcoming_dvds`<a id="rottentomatoesdvd_listsget_upcoming_dvds"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.dvd_lists.get_upcoming_dvds(
    page_limit="16",
    page="1",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_limit: `str`<a id="page_limit-str"></a>

The amount of upcoming dvds to show per page

##### page: `str`<a id="page-str"></a>

The selected page of upcoming DVDs

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/dvds/upcoming.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.detailed_info.find_similar_movies`<a id="rottentomatoesdetailed_infofind_similar_movies"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.detailed_info.find_similar_movies(
    id="770672122",
    limit="5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID

##### limit: `str`<a id="limit-str"></a>

Limit the number of similar movies to show

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movies/{id}/similar.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.detailed_info.get_clip_by_id`<a id="rottentomatoesdetailed_infoget_clip_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.detailed_info.get_clip_by_id(
    id="770672122",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movies/{id}/clips.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.detailed_info.get_movie_alias_info`<a id="rottentomatoesdetailed_infoget_movie_alias_info"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.detailed_info.get_movie_alias_info(
    id="0031381",
    type="imdb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID

##### type: `str`<a id="type-str"></a>

Only supports imdb lookup at this time

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movie_alias.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.detailed_info.get_movie_by_id_json`<a id="rottentomatoesdetailed_infoget_movie_by_id_json"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.detailed_info.get_movie_by_id_json(
    id="770672122",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movies/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.detailed_info.get_movie_cast`<a id="rottentomatoesdetailed_infoget_movie_cast"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.detailed_info.get_movie_cast(
    id="770672122",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movies/{id}/cast.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.detailed_info.get_movie_reviews`<a id="rottentomatoesdetailed_infoget_movie_reviews"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.detailed_info.get_movie_reviews(
    id="770672122",
    review_type="top_critic",
    page_limit="20",
    page="1",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID

##### review_type: `str`<a id="review_type-str"></a>

3 different review types are possible: 'all', 'top_critic' and 'dvd'. 'top_critic' shows all the Rotten Tomatoes designated top critics. 'dvd' pulls the reviews given on the DVD of the movie. 'all' as the name implies retrieves all reviews.

##### page_limit: `str`<a id="page_limit-str"></a>

The number of reviews to show per page

##### page: `str`<a id="page-str"></a>

The selected page of reviews

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movies/{id}/reviews.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.movie_lists.get_box_office_json`<a id="rottentomatoesmovie_listsget_box_office_json"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.movie_lists.get_box_office_json(
    limit="16",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

Limits the number of movies returned

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/movies/box_office.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.movie_lists.get_intheater_movies`<a id="rottentomatoesmovie_listsget_intheater_movies"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.movie_lists.get_intheater_movies(
    page_limit="16",
    page="1",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_limit: `str`<a id="page_limit-str"></a>

The amount of movies in theaters to show per page

##### page: `str`<a id="page-str"></a>

The selected page of in theaters movies

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/movies/in_theaters.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.movie_lists.get_opening_movies`<a id="rottentomatoesmovie_listsget_opening_movies"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.movie_lists.get_opening_movies(
    limit="16",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

Limits the number of opening movies returned

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/movies/opening.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.movie_lists.get_upcoming_movies`<a id="rottentomatoesmovie_listsget_upcoming_movies"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.movie_lists.get_upcoming_movies(
    page_limit="16",
    page="1",
    country="us",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_limit: `str`<a id="page_limit-str"></a>

The amount of upcoming movies to show per page

##### page: `str`<a id="page-str"></a>

The selected page of upcoming movies

##### country: `str`<a id="country-str"></a>

Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/movies/upcoming.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.search.movies_json`<a id="rottentomatoessearchmovies_json"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.search.movies_json(
    q="string_example",
    page_limit="10",
    page="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The plain text search query to search for a movie. Remember to URI encode this!

##### page_limit: `str`<a id="page_limit-str"></a>

The amount of movie search results to show per page

##### page: `str`<a id="page-str"></a>

The selected page of movie search results

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/movies.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.top_level_lists.get_data`<a id="rottentomatoestop_level_listsget_data"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.top_level_lists.get_data()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.top_level_lists.get_dvds`<a id="rottentomatoestop_level_listsget_dvds"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.top_level_lists.get_dvds()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/dvds.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `rottentomatoes.top_level_lists.get_movies_json`<a id="rottentomatoestop_level_listsget_movies_json"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rottentomatoes.top_level_lists.get_movies_json()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/movies.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
