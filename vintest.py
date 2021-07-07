import unittest
import requests
from vin import parse_data, get_auth

DECODE_URL = 'http://api.carmd.com/v3.0/decode?vin='

class TestFileName(unittest.TestCase):
    def test_parse_data(self):
        headers = get_auth()
        self.assertFalse(parse_data(requests.get(DECODE_URL + '12345678912345678', headers=headers).json()))

#     def test_get_auth(self):
#         self.assertEqual(function2(2,1), 3)
#         self.assertEqual(function2(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()