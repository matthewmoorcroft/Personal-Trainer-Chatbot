import unittest
from connections.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database.get_instance()
        cur = self.database.conn.cursor()

        cur.execute("""INSERT INTO core.users (id, name, age, gender, telegram_id)
                    VALUES(0, 'test', 23, 'male', 0)""")

        self.database.conn.commit()

    def test_check_user(self):
        tests = [
            (1234, None),
            (0, None)
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                result = self.database.check_user(value)
                self.assertEqual(result, expected)

    def tearDown(self):
        cur = self.database.conn.cursor()

        cur.execute("""DELETE FROM core.users WHERE id = 0""")

        self.database.conn.commit()


if __name__ == '__main__':
    unittest.main()
