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

        def test_add_user(self):
            measurements = {
                'weight': 82,
                'bodyfatratio': 0,
                'c_chest': 0,
                'c_leg': 0,
                'c_waist': 0,
                'c_triceps': 0
            }
            user_test1 = {
                'name': 'test',
                'age': 0,
                'gender': 'male',
                'telegram_id': '1111',
                'measurements': measurements
            }
            result_test1 = {
                'result': 'ok'
            }
            result_test2 = {
                'result': "Error: Not all fields filled"
            }

            tests = [
                (user_test1, result_test1),
                (None, result_test2)
            ]
            for value, expected in tests:
                with self.subTest(value=value):
                    result = self.database.add_user(value)
                    self.assertEqual(result, expected)

            def test_delete_user(self):
                result_test1 = {'result': 'ok'}
                tests = [
                    (0, result_test1),
                    (0, None)
                ]
                for value, expected in tests:
                    with self.subTest(value=value):
                        result = self.database.delete_user(value)
                        self.assertEqual(result, expected)

    def tearDown(self):
        cur = self.database.conn.cursor()

        cur.execute("""DELETE FROM core.users WHERE id = 0""")

        self.database.conn.commit()


if __name__ == '__main__':
    unittest.main()
