# auth.py
import falcon
import base64


class AuthHandler(object):

    def parse_auth_details(self, req, auth_details):
        auth_details = base64.b64decode(auth_details).decode('utf-8')
        username, key = auth_details.split(':', 1)
        username = username.strip()
        key = key.strip()
        req.context['auth.username'] = username
        req.context['auth.password'] = key

    def check_auth(self, req, resp, resource, params):
        # Allow all options requests
        if req.method == 'OPTIONS':
            return
        # Do we need auth? Check the resources public methods
        if hasattr(resource, 'PUBLIC_METHODS'):
            if req.method in resource.PUBLIC_METHODS:
                return

        # otherwise, if no attempt at auth, request auth
        if not req.auth:
            raise falcon.HTTPUnauthorized(
                "Authentication Required",
                "Provide credentials",
                challenges=['ApiAuth realm="JimdoAPI"']
            )
        try:
            auth_type, auth_details = req.auth.split(' ', 1)
        except Exception as Ex:
            raise falcon.HTTPUnauthorized(
                'Authentication Error',
                'Provide valid credentials',
                challenges=['ApiAuth realm="JimdoAPI"']
            )

        try:
            self.parse_auth_details(req, auth_details)
        except Exception as Ex:
            raise falcon.HTTPUnauthorized(
                'Authentication Error',
                'Provide valid credentials',
                challenges=['ApiAuth realm="JimdoAPI"']
            )

    def process_resource(self, req, resp, resource, params):
        self.check_auth(req, resp, resource, params)

        resource.user = None

        # Allow all options requests
        if req.method == 'OPTIONS':
            return

        if resource is None:
            return

        # Process user details
        username = ''
        password = ''
        if 'auth.username' in req.context:
            username = req.context['auth.username']
        if username:
            resp.set_header('WWW-Authenticate', '')

        if 'auth.password' in req.context:
            password = req.context['auth.password']

        resource.user = self.get_user(
            username,
            password
        )

        # Allow explicitly declared public URIs
        if hasattr(resource, 'PUBLIC_METHODS'):
            if req.method in resource.PUBLIC_METHODS:
                return

        if not resource.user:
            raise falcon.HTTPUnauthorized(
                'Authentication Error',
                'Provide valid credentials',
                challenges=['ApiAuth realm="JimdoAPI"']
            )

    # Given the username and password, return the user details
    # return None if user auth fails
    def get_user(self, username, password):

        user = {}
        
        if username == "bqube@test.com":
            user["username"] = username
        else:
            return None
        
        if password == "f1c4a87883ee87f5e4cc420bcd2f1f115683dfb82127759e909056e7fa390eb7":
            user["password"] = password
        else: 
            return None

        return user

