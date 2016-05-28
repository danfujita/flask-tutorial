import unittest
from unittest.mock import MagicMock
from app import app
import users

class TestStringMethods(unittest.TestCase):
    @app.before_request
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get(self):
        user = {}
        self.app.get_users_db = MagicMock()
        self.app.get_users_db.return_value = user
        print (self.app.get_users_db())
        result = self.app.get('/users/danfujita')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
