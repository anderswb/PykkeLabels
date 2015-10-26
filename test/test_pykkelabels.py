# -*- coding: utf-8 -*-

import unittest
from pykkelabels import Pykkelabels

import urllib.error
from decimal import *
import base64
import configparser
from os import path


class GoodInput(unittest.TestCase):

    def test_login(self):
        try:
            Pykkelabels(self.api_user, self.api_key)
        except urllib.error.HTTPError:
            self.fail('Did not log in properly')

    def test_balance(self):
        pl = Pykkelabels(self.api_user, self.api_key)
        self.assertEqual(Decimal(0.0), pl.balance())

    def test_getToken(self):
        pl = Pykkelabels(self.api_user, self.api_key)
        self.assertEqual(40, len(pl.getToken()))

    def test_pdkdroppoints(self):
        pl = Pykkelabels(self.api_user, self.api_key)
        exp_points = [{'zipcode': '2300', 'city': 'KØBENHAVN S', 'address': 'Brydes Allé 34', 'number': '3830',
                       'company_name': 'Pakkeboks 3830 Dagli Brugsen'},
                      {'zipcode': '2300', 'city': 'KØBENHAVN S', 'address': 'Englandsvej 28', 'number': '626',
                       'company_name': 'Pakkeboks 626 Kvickly'},
                      {'zipcode': '2300', 'city': 'KØBENHAVN S', 'address': 'Englandsvej 28', 'number': '626',
                       'company_name': 'Pakkeboks 626 Kvickly Handikapvenlig'}]
        points = pl.pdk_droppoints({'zipcode': '2300'})
        self.assertEqual(points, exp_points)

    def test_glsdroppoints(self):
        pl = Pykkelabels(self.api_user, self.api_key)
        exp_points = [{'number': '95913', 'city': 'København S', 'company_name': 'Dagli´Brugsen Brydes Allé',
                       'address2': 'Pakkeshop: 95913', 'address': 'Brydes\xa0Allé 34', 'zipcode': '2300'},
                      {'number': '95422', 'city': 'København S', 'company_name': 'PC Update',
                       'address2': 'Pakkeshop: 95422', 'address': 'Amagerbrogade 109', 'zipcode': '2300'},
                      {'number': '95423', 'city': 'København S', 'company_name': 'Centerkiosken',
                       'address2': 'Pakkeshop: 95423', 'address': 'Reberbanegade 3', 'zipcode': '2300'}]
        points = pl.gls_droppoints({'zipcode': '2300'})
        self.assertEqual(points, exp_points)

    def test_freight_rates(self):
        pl = Pykkelabels(self.api_user, self.api_key)
        rates = pl.freight_rates()

        # Test a couple of things, which should be in the returned dict
        self.assertIsInstance(rates, dict)
        self.assertIsInstance(rates['DK'], dict)
        self.assertIsInstance(rates['GB'], dict)
        self.assertIsInstance(rates['DE'], dict)
        self.assertIsInstance(rates['DK']['gls'], dict)
        self.assertIsInstance(rates['DK']['pdk'], dict)
        self.assertEqual(rates['DK']['pdk']['name'], 'Post Danmark')

    def test_payment_requests(self):
        pl = Pykkelabels(self.api_user, self.api_key)
        requests = pl.payment_requests()
        self.assertIsInstance(requests, list)
        self.assertEqual(0, len(requests))

    def test_create_shipment(self):
        params = {'shipping_agent': 'pdk',
                  'weight': '1000',
                  'receiver_name': 'John Doe',
                  'receiver_address1': 'Some Street 42',
                  'receiver_zipcode': '5230',
                  'receiver_city': 'Odense M',
                  'receiver_country': 'DK',
                  'receiver_email': 'test@test.dk',
                  'receiver_mobile': '12345678',
                  'sender_name': 'John Wayne',
                  'sender_address1': 'The Batcave 1',
                  'sender_zipcode': '5000',
                  'sender_city': 'Odense C',
                  'sender_country': 'DK',
                  'shipping_product_id': '51',
                  'services': '11,12',
                  'test': 'true'}

        pl = Pykkelabels(self.api_user, self.api_key)
        result = pl.create_shipment(params)
        self.assertEqual(result['pkg_no'], '00000000000000000000')
        self.assertEqual(result['order_id'], '0000')
        self.assertEqual(result['shipment_id'], '0000')
        pdfpayload = base64.b64decode(result['base64'])

        # test that the retrieved data seems pdf-ish
        self.assertEqual(pdfpayload[0:7], b'%PDF-1.')

    def setUp(self):
        try:
            config = configparser.ConfigParser()
            if path.isfile('test/testsettings.ini'):
                config.read('test/testsettings.ini')
            elif path.isfile('testsettings.ini'):
                config.read('testsettings.ini')
            else:
                raise Exception('Missing testsettings.ini file')
            self.api_user = config.get('login', 'api_user')
            self.api_key = config.get('login', 'api_key')
        except:
            raise Exception('Unable to read the required settings from the ini file.')


if __name__ == '__main__':
    unittest.main()
