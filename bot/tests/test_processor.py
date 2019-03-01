import unittest
from controller.processor import text_normalization
# from unittest.mock import patch
# import requests_mock


class TestProcessor(unittest.TestCase):

    def test_text_normalization(self):
        tests = [
            ('hello', 'hello'),
            ('HELLO', 'hello'),
            ('$Hello', '$hello'),
            ('2123', '2123')
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(text_normalization(value), expected)

    # def test_process_message(self):
    #
    #     json_resp_welcome = {
    #         'intent': 'welcome',
    #         'variables': '',
    #         'response': ["""Hey, I don't seem to know you. Do you want me to
    #                         help you out with your training?"""],
    #         'finished': False
    #     }
    #     json_resp_normal = {
    #         'intent': 'help',
    #         'variables': '',
    #         'response': ['These are the things I can help you out with'],
    #         'finished': True
    #     }
    #     query_result = [("id", 1234),
    #                     ("name", "Matthew"),
    #                     ("age", 23),
    #                     ("gender", "male"),
    #                     ("telegram_id", "1111"),
    #                     ("weight", 82.5),
    #                     ("bodyfatratio", 82.5),
    #                     ("c_chest", 82.5),
    #                     ("c_leg", 82.5),
    #                     ("c_waist", 82.5),
    #                     ("c_triceps", 82.5)]
    #
    #     with requests_mock.Mocker() as m:
    #         m.register_uri('POST', 'http://localhost:30000/process_welcome',
    #                        json=json_resp_welcome)
    #         m.register_uri('POST', 'http://localhost:30000/process_message',
    #                        json=json_resp_normal)
    #
    #         with mock.patch('psycopg2.connect') as mock_connect:
    #             mock_connect.cursor.return_value.execute.fetch_all = qry_result
    #
    #             raw_message = {
    #
    #             }
    #     for value, expected in tests:
    #         with self.subTest(value=value):
    #             self.assertEqual(text_normalization(value), expected)

    # def test_mock (self):
        # with patch('employee.requests.get') as mocked_get:
        # mocked_get.return_value.ok = True
        # mocked_get.return_value = 'Success'

        # schedulte = self.emp_1.monthly_shedule('May')
        # mocked_get.assert_called_with('http://company.com/Schafer/May')
        # self.assertEqual(schedule, 'Success')

        # with patch('employee.requests.get') as mocked_get:
        # mocked_get.return_value.ok = False
        # mocked_get.return_value = 'Bad response!'

        # schedulte = self.emp_2.monthly_shedule('June')
        # mocked_get.assert_called_with('http://company.com/Smith/June')
        # self.assertEqual(schedule, 'Bad response!')


if __name__ == '__main__':
    unittest.main()
