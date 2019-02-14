import unittest
from connections.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    def test_get_instance(self):
        self.assertEqual(self.database.get_instance(), self.database)

    def tearDown(self):
        self.database = None


if __name__ == '__main__':
    unittest.main()
