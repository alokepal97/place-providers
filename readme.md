# Project Description for Jimdo Places API

**dependencies**
- Python(>=3.6)
- Falcon(microservice framework)
- gunicorn(for wsgi server)
- nose2(as a unit test framework)

**To run the project, within project folder**

`gunicorn api.app:app`

**To run the test, within project folder >api>**

`nose2`

### You can test basic api connectivity

`http://127.0.0.1:8000/1.0/ping`

**Returns**
```
    "Easter eggs"
```
## Authentication

Any endpoint requiring an authenticated user but not having one will return `401 Unauthorized`.
Authentication is performed in the same way as HTTP Basic authentication but with the scheme "ApiAuth" rather than "Basic". This is now hardcoded but can be easily implemented with data from database, if you using REST client like Insomnia or Postman, please use
```
    username: bqube@test.com
    password: f1c4a87883ee87f5e4cc420bcd2f1f115683dfb82127759e909056e7fa390eb7
```
for http header use,
```
-H "authorization: ApiAuth YnF1YmVAdGVzdC5jb206ZjFjNGE4Nzg4M2VlODdmNWU0Y2M0MjBiY2QyZjFmMTE1NjgzZGZiODIxMjc3NTllOTA5MDU2ZTdmYTM5MGViNw=="
```
### Authentication Implementation

All routes by default require an authenticated user except those which are marked as a `PUBLIC_METHODS`

## Api Endpoints

### `GET` /1.0/places
to get places depends on keyword provided

**Required authorization** 

True

**Parameters**

- `input(required)`: any string to search
- `ll(optional)`: latitude and longitude, comma separeted like,
```
&ll=22.7509969,88.3467107
```
- `radius(optional)`: default radius set 250, if provided it simply overright itself

**Response**
```
{
    "places": [
		{
			"ID": "ChIJW6j1EyKb-DkR4qZ08SKtLjo",
			"Provider": "Google API",
			"Name": "Serampore",
			"Description": {
				"photos": [
					{
						"height": 564,
						"html_attributions": [
							"<a href=\"https://maps.google.com/maps/contrib/116666205521980994652/photos\">Subhayan Mukherjee [TITO]</a>"
						],
						"photo_reference": "CmRaAAAApdpoWCScKcvKbnVvHhY7RTDmoCpQo3_sxV36Lb71yZZUuicVcqd6DiYhXsU0hHX4U4WPtBD0CgRSYT1Sy01TZWXndbyHDd1Y_mR6Tl9VGSosDK65OfTzjdTAUoYeyB8lEhAqhXBjrLgyEgwNhb_eXSp6GhSICge_VQU8gl5r6GH0k2U0OZ_4IA",
						"width": 960
					}
				],
				"types": [
					"sublocality_level_1",
					"sublocality",
					"political"
				]
			},
			"Location": {
				"lat": 22.748331,
				"lng": 88.3385053
			},
			"Address": "West Bengal, India",
			"URI": ""
		}
	],
	"status": "OK"
}
```

### `GET` /1.0/places/{vendor}
to get places depends on keyword provided from a desired places data provider, like google places api.
Right this time this api can only access `google` places api

**Required authorization** 

True

**Parameters**

- `vendor(optional)`: *google*
- `input(required)`: any string to search
- `ll(optional)`: latitude and longitude, comma separeted like,
```
&ll=22.7509969,88.3467107
```
- `radius(optional)`: default radius set 250, if provided it simply overright itself

**Response**

Similar data like the above demo response











