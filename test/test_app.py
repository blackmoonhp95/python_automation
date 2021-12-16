import unittest
from api_app import api_app
import json


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = api_app.app.test_client()

    def test_hello_world_testcase1(self):
        """
        Test GET request
        :return:
        """
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode('utf-8'), str('Hello World'))

    def test_hello_world_testcase2(self):
        """
        Test POST request success
        :return:
        """
        data_json = json.dumps(dict(valid='True'))
        response = self.app.post('/hello', data=data_json, content_type='application/json')

        json_response = response.json
        self.assertEqual(json_response, dict(code=200, message='Success Request'))

    def test_hello_world_testcase3(self):
        """
        Test POST request error
        :return:
        """
        response = self.app.post('/hello')

        json_response = response.json
        self.assertEqual(json_response, dict(code=500, message='Error'))

    def test_hello_world_testcase4(self):
        """
        Test POST request invalid
        :return:
        """
        data_json = json.dumps(dict(another_key='True'))
        response = self.app.post('/hello', data=data_json, content_type='application/json')

        json_response = response.json
        self.assertEqual(json_response, dict(code=403, message='Invalid Request'))

if __name__ == '__main__':
    unittest.main()