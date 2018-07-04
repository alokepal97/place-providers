# places.py
import falcon
import json

from api.lib.google_api import GoogleAPI
# from api.lib.fourquare_api import FourSquareAPI

class PlacesApi(object):

    def on_get(self, req, resp, vendor=None):
        if "input" not in req.params:
            resp.status = falcon.HTTP_400
            return

        googleApi = GoogleAPI()
        # fourSApi = FourSquareAPI()

        # If no vendor passed, we use google maps api as default
        if not vendor:
            output = googleApi.create_request(req.params)

        # using the desired map provider
        if vendor == "google":
            output = googleApi.create_request(req.params)

        # if vendor == "foursqare":
        #     output = fourSApi.create_request(req.params)
       
        # Return script data
        # if length of places is 0, change the http status code or leave to default 200
        if len(output['places']) == 0:
            resp.status = falcon.HTTP_204

        resp.body = json.dumps(output)