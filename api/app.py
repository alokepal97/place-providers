import falcon

from api.middleware.auth import AuthHandler
from api.routes.places import PlacesApi
from api.routes.ping import Ping

class Api():

    API_VERSION = '1.0'

    def create_app(self):

        # Middleware
        self.auth = AuthHandler()

        # Create our WSGI app instance
        self.api = falcon.API(middleware=[
            self.auth
        ])

        # API components
        ping = Ping()
        places = PlacesApi()

        # Routes
        web = self.api
        ver = self.API_VERSION
        # Ping test and routes
        web.add_route('/' + ver + '/ping', ping)
        # google maps
        web.add_route('/' + ver + '/places/{vendor}', places) 
        web.add_route('/' + ver + '/places', places)

        return self.api


instance = Api()
app = instance.create_app()
