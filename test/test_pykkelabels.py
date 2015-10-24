import unittest
from pykkelabels.pykkelabels import *

import urllib.error
from decimal import *

API_USER = '492ace80-8b40-4369-8ee7-ca4457984ffb'
API_KEY = 'da04a9e9-1563-4aaf-b443-3012ca6c2772'

class goodinput(unittest.TestCase):

    def test_login(self):
        try:
            Pykkelabels(API_USER, API_KEY)
        except urllib.error.HTTPError:
            self.fail('Did not log in properly')

    def test_balance(self):
        pl = Pykkelabels(API_USER, API_KEY)
        self.assertEquals(Decimal(0.0), pl.balance())

    def test_getToken(self):
        pl = Pykkelabels(API_USER, API_KEY)
        self.assertEquals(40, len(pl.getToken()))

if __name__ == '__main__':
    unittest.main()