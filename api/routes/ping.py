# ping.py
import json


class Ping():

    PUBLIC_METHODS = ['GET']

    def on_get(self, req, resp):
        # Return "Easter eggs"
        resp.body = json.dumps("Easter eggs")
