import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client using Flask's test_client() method
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass  # Optional: Clean up after test cases, if needed

    def test_hello_route(self):
        # Make a GET request to the / route
        response = self.app.get('/')
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data matches the expected output
        self.assertEqual(response.data.decode('utf-8'), "I am almost a Devops Engineer!")

if __name__ == '__main__':
    unittest.main()
