#<?php
#
#/*
#Usage:
#----------------
#The first thing required is to login
#label = new Pakkelabels('api_user', 'api_key'); 
#
#This will login and fetch the required token. 
#The token is then automatically added to any subsequent calls. 
#
#To see the generated token you can use:
#echo label->getToken();
#
#Examples:
#----------------
#// Get all Post Danmark labels shipped to Denmark
#labels = label->shipments(array('shipping_agent' => 'pdk', 'receiver_country' => 'DK'));
#
#// Display the PDF for a specific label
#base64 = label->pdf(31629);
#pdf = base64_decode(base64);
#header('Content-type: application/pdf');
#header('Content-Disposition: inline; filename="label.pdf"');
#echo pdf;
#*/
#

import urllib.request
import urllib.error
import urllib.parse
import json

class Pykkelabels:
    API_ENDPOINT = 'https://app.pakkelabels.dk/api/public/v2'

    def __init__(self, api_user, api_key):
        self._api_user = api_user
        self._api_key = api_key
        self._token = None
        self.login()

    def login(self):
        result = self._make_api_call('users/login', True, {'api_user': self._api_user, 'api_key': self._api_key})
        self._token = result['token']

    def balance(self):
        result = self._make_api_call('users/balance')
        return result['balance']

    def pdf(self, id):
        result = self._make_api_call('shipments/pdf', False, {'id': id})
        return result['base64']

    def zpl(self, id):
        result = self._make_api_call('shipments/zpl', False, {'id': id})
        return result['base64']
    
    def shipments(self, params = dict()):
        result = self._make_api_call('shipments/shipments', False, params)
        return result
    
    def imported_shipments(self, params = dict()):
        result = self._make_api_call('shipments/imported_shipments', False, params)
        return result

    def create_imported_shipment(self, params):
        result = self._make_api_call('shipments/imported_shipment', True, params)
        return result
    
    def create_shipment(self, params):
        result = self._make_api_call('shipments/shipment', True, params)
        return result

    def create_shipment_own_customer_number(self, params):
        result = self._make_api_call('shipments/shipment_own_customer_number', True, params)
        return result

    def freight_rates(self):
        result = self._make_api_call('shipments/freight_rates')
        return result

    def payment_requests(self):
        result = self._make_api_call('users/payment_requests')
        return result

    def gls_droppoints(self, params):
        result = self._make_api_call('shipments/gls_droppoints', False, params)
        return result

    def pdk_droppoints(params):
        result = self._make_api_call('shipments/pdk_droppoints', False, params)
        return result

    def getToken(self):
        return self._token

    def _make_api_call(self, method, doPost = False, params = dict()):
        params['token'] = self._token
        params = urllib.parse.urlencode(params)
        
        if doPost:
            url = Pykkelabels.API_ENDPOINT + '/' + method
            f = urllib.request.urlopen(url, params.encode('utf-8'))
        else:
            url = Pykkelabels.API_ENDPOINT + '/' + method + '?' + params
            f = urllib.request.urlopen(url)

#        curl_setopt(ch, CURLOPT_RETURNTRANSFER, true);

#        http_code = curl_getinfo( ch, CURLINFO_HTTP_CODE);

        output = f.read().decode('utf-8')
        outputparsed = json.loads(output)

#        if http_code != 200:
#            if(is_array(output['message'])):
#                    print_r(output['message']);
#                    die();
#            }else{
#                    die(output['message']);
#            }
        return outputparsed


if __name__ == '__main__':
    pl = Pykkelabels('871684fe-b098-4d04-a96a-527865f162da', '073e628f-c8b6-4911-87b5-63b6fa451fc6')
    print('Token: {}'.format(pl.getToken()))
    print('Balance: {}'.format(pl.balance()))
    print('GLS droppoints:')
    for droppoint in pl.gls_droppoints({'zipcode': '2300'}):
        print(' ------------------')
        for key, value in droppoint.items():
            print(' ' + key + ': ' + value)
    #print(pl.freight_rates())
    
