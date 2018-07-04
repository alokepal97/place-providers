# google_api.py

import requests, json


class GoogleAPI(object):

    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    API_KEY = "AIzaSyC1ssS6ueb8-X2a22lPW4r1_QGLTn3Ds_c"
    BUILD_QUERY = {}
    RAD = 250
    RESP = [
        'formatted_address',
        'place_id',
        'geometry',
        'name',
        'photos',
        'types'
    ]

    def create_request(self, queryData):
        if "input" in queryData:
            self.BUILD_QUERY['query'] = queryData['input']

        # set provided radius to RAD
        if "radius" in queryData:
            self.RAD = queryData["radius"]

        # build locationbiased string, if there ll provided
        if "ll" in queryData:
            self.BUILD_QUERY['location'] = ','.join(queryData['ll'])
            self.BUILD_QUERY['radius'] = self.RAD

        # self.BUILD_QUERY['fields'] = ','.join(self.RESP)
        self.BUILD_QUERY['key'] = self.API_KEY
        
        # call google api to get places data
        resp = self.__do_request()
        
        # return response in our desired way
        return self.__make_response(resp)


    # building the request using query parameters
    def __do_request(self):
        r = requests.get(self.URL, self.BUILD_QUERY)
        resp = r.json()
        return resp


    # modify the response such that the data having only
    # ID, Provider, Name, Description, Location (lat, lng) (if applicable), Address (if applicable), URI of the place where more details are available
    def __make_response(self, resp):
        # temporary list for our modified data
        output = {}
        temp = []
        
        if resp['status'] == "OK":
            for x in resp['results']:
                d = {
                    'ID' : '',
                    'Provider' : '',
                    'Name' : '',
                    'Description' : {},
                    'Location' : '',
                    'Address' : '',
                    'URI' : ''
                }
                d['ID'] = x['place_id']
                d['Provider'] = "Google API"
                d['Name'] = x['name']
                if "photos" in x:
                    d['Description']['photos'] = x['photos']
                if "types" in x:
                    d['Description']['types'] = x['types']

                d['Location'] = x['geometry']['location']
                d['Address'] = x['formatted_address']

                d['URI'] = ""
                temp.append(d)
            # make the response object    
            output = {
                'places' : temp,
                'status' : "OK"
            }
        elif resp['status'] == "INVALID_REQUEST":
            output = {
                'places' : temp,
                'status' : "the query is missing"
            }
        elif resp['status'] == "NOT_FOUND":
            output = {
                'places' : temp,
                'status' : "the referenced location was not found "
            }
        else:
            output = {
                'places' : temp,
                'status' : "No Data Found"
            }

        return output