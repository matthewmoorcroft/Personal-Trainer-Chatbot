import unittest
from controller.processor import *

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
    #     tests = [
    #         ('hello', 'hello'),
    #         ('HELLO', 'hello'),
    #         ('$Hello', '$hello'),
    #         ('2123', '2123')
    #     ]
    #     for value, expected in tests:
    #         with self.subTest(value=value):
    #             self.assertEqual(text_normalization(value), expected)



if __name__ == '__main__':
    unittest.main()
