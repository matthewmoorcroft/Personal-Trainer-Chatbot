from connections import mlengine
import unittest
import json


class TestNetManager(unittest.TestCase):

    def test_send_message(self):

        result = mlengine.send_message("test_message", 375033117)
        self.assertEqual(json.dumps(result), json.dumps({'result': "ok"}))
