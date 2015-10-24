# -*- coding: utf-8 -*-

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
        self.assertEqual(Decimal(0.0), pl.balance())

    def test_getToken(self):
        pl = Pykkelabels(API_USER, API_KEY)
        self.assertEqual(40, len(pl.getToken()))

    def test_pdkdroppoints(self):
        pl = Pykkelabels(API_USER, API_KEY)
        exp_points = [{'zipcode': '2300', 'city': 'KØBENHAVN S', 'address': 'Brydes Allé 34', 'number': '3830',
                       'company_name': 'Pakkeboks 3830 Dagli Brugsen'},
                      {'zipcode': '2300', 'city': 'KØBENHAVN S', 'address': 'Englandsvej 28', 'number': '626',
                       'company_name': 'Pakkeboks 626 Kvickly'},
                      {'zipcode': '2300', 'city': 'KØBENHAVN S', 'address': 'Englandsvej 28', 'number': '626',
                       'company_name': 'Pakkeboks 626 Kvickly Handikapvenlig'}]
        points = pl.pdk_droppoints({'zipcode': '2300'})
        self.assertEqual(points, exp_points)

    def test_glsdroppoints(self):
        pl = Pykkelabels(API_USER, API_KEY)
        exp_points = [{'number': '95913', 'city': 'København S', 'company_name': 'Dagli´Brugsen Brydes Allé',
                       'address2': 'Pakkeshop: 95913', 'address': 'Brydes\xa0Allé 34', 'zipcode': '2300'},
                      {'number': '95422', 'city': 'København S', 'company_name': 'PC Update',
                       'address2': 'Pakkeshop: 95422', 'address': 'Amagerbrogade 109', 'zipcode': '2300'},
                      {'number': '95423', 'city': 'København S', 'company_name': 'Centerkiosken',
                       'address2': 'Pakkeshop: 95423', 'address': 'Reberbanegade 3', 'zipcode':'2300'}]
        points = pl.gls_droppoints({'zipcode': '2300'})
        self.assertEqual(points, exp_points)

if __name__ == '__main__':
    unittest.main()