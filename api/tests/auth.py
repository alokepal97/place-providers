# auth.py
import base64
import hashlib


class TestAuth():

    @classmethod
    def get(cls, username='bqube@test.com', password='f1c4a87883ee87f5e4cc420bcd2f1f115683dfb82127759e909056e7fa390eb7'):
        # password = (username + password).encode("utf-8")
        # password = hashlib.sha256(password).hexdigest()
        authdetails = username + ':' + password
        authdetails = base64.b64encode(authdetails.encode('utf-8')).decode()
        # authdetails = base64.b64encode(authdetails)
        auth = {
            'authorization': 'ApiAuth ' + authdetails
        }
        return auth
