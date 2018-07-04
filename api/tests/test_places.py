from falcon import testing
from api.app import Api
from api.tests.auth import TestAuth



class ApiTest(testing.TestCase):
    def setUp(self):
        super(ApiTest, self).setUp()
        self.api = Api()
        api = self.api
        self.API_VERSION = self.api.API_VERSION
        self.app = self.api.create_app()
  

class TestGoogleApi(ApiTest):

    def test_parameterMissingError(self):

        result = self.simulate_get('/' + self.API_VERSION + '/places/', headers = TestAuth.get())
        self.assertEqual(result.status_code, 400)

    def test_parameterSuccess(self):

    	result = self.simulate_get('/' + self.API_VERSION + '/places/google/',
    	headers = TestAuth.get(), query_string = "input=restaurants+in+Sydney")
    	self.assertEqual(result.status_code, 200)

    def test_parameterLatitudeSuccess(self):

    	result = self.simulate_get('/' + self.API_VERSION + '/places/',
    	headers = TestAuth.get(), query_string = "input=restaurants+in+kolkata&ll=22.6498266,88.2529764&radius=100")
    	self.assertEqual(result.status_code, 200)

    def test_parameterPlacesFail(self):

    	result = self.simulate_get('/' + self.API_VERSION + '/places/',
    	headers = TestAuth.get(), query_string = "input=opgkpijaoijoij&ll=22.6498266,88.2529764&radius=100")
    	self.assertEqual(result.status_code, 204)