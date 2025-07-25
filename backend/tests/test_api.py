import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello from Flask backend!"})

if __name__ == '__main__':
    unittest.main()