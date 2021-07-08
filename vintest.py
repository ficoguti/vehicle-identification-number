import unittest
import requests
from vin import parse_data, get_auth, createDataFrame, loadDataset
from vin import createEngine


DECODE_URL = 'http://api.carmd.com/v3.0/decode?vin='


class TestFileName(unittest.TestCase):
    def test_parse_data(self):
        headers = get_auth()
        self.assertEqual(parse_data('12345678912345678'), None)

    def test_get_auth(self):
        headers = {
            "content-type": "application/json",
            "authorization": 'Basic ' +
            'ODYwYmMxNjQtNjE3OS00OGM5LWEwZGYtN2FkZTQ4ZjY0NmE3',
            "partner-token": 'cddae0cb72134c408a0836016130be55'
        }

        self.assertEqual(get_auth(), headers)

    def test_createDataFrame(self):
        r = {'data': {'year': 1999, 'make': 'FORD', 'model': 'TAURUS',
             'manufacturer': 'FORD', 'engine': 'V6, 3.0L', 'trim': 'LX',
                      'transmission': 'AUTOMATIC'}}
        df = createDataFrame(r, '12345678912345678')
        self.assertFalse(df.empty)

#     def test_createEngine(self):
#         self.assertNotEqual(createEngine('test'), None)

#     def test_loadDataset(self):
#         df = loadDataset('vindecoder', 'queries', 'vin-queries.sql')
#         self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()
