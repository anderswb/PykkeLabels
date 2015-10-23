#<?php
#
#/*
#Usage:
#----------------
#The first thing required is to login
#$label = new Pakkelabels('api_user', 'api_key'); 
#
#This will login and fetch the required token. 
#The token is then automatically added to any subsequent calls. 
#
#To see the generated token you can use:
#echo $label->getToken();
#
#Examples:
#----------------
#// Get all Post Danmark labels shipped to Denmark
#$labels = $label->shipments(array('shipping_agent' => 'pdk', 'receiver_country' => 'DK'));
#
#// Display the PDF for a specific label
#$base64 = $label->pdf(31629);
#$pdf = base64_decode($base64);
#header('Content-type: application/pdf');
#header('Content-Disposition: inline; filename="label.pdf"');
#echo $pdf;
#*/
#

import urllib.request
import urllib.error

class Pykkelabels:
    API_ENDPOINT = 'https://app.pakkelabels.dk/api/public/v2'

    def __init__(self, api_user, api_key):
        self._api_user = api_user
        self._api_key = api_key
        self.login()

    def login(self):
        # Create an OpenerDirector with support for Basic HTTP Authentication...
        auth_handler = urllib.request.HTTPBasicAuthHandler()
        auth_handler.add_password(None, Pykkelabels.API_ENDPOINT, self._api_user, self._api_key);
        
        opener = urllib.request.build_opener(auth_handler)
        # ...and install it globally so it can be used with urlopen.
        urllib.request.install_opener(opener)

#    public function balance(){
#        $result = $this->_make_api_call('users/balance');
#        return $result['balance'];
#    }
#
#    public function pdf($id){
#        $result = $this->_make_api_call('shipments/pdf', false, array('id' => $id));
#        return $result['base64'];
#    }
#
#    public function zpl($id){
#        $result = $this->_make_api_call('shipments/zpl', false, array('id' => $id));
#        return $result['base64'];
#    }
#    
#    public function shipments($params = array()){
#        $result = $this->_make_api_call('shipments/shipments', false, $params);
#        return $result;
#    }
#    
#    public function imported_shipments($params = array()){
#        $result = $this->_make_api_call('shipments/imported_shipments', false, $params);
#        return $result;
#    }
#
#    public function create_imported_shipment($params){
#        $result = $this->_make_api_call('shipments/imported_shipment', true, $params);
#        return $result;
#    }
#    
#    public function create_shipment($params){
#        $result = $this->_make_api_call('shipments/shipment', true, $params);
#        return $result;
#    }
#
#    public function create_shipment_own_customer_number($params){
#        $result = $this->_make_api_call('shipments/shipment_own_customer_number', true, $params);
#        return $result;
#    }
#
#    public function freight_rates(){
#        $result = $this->_make_api_call('shipments/freight_rates');
#        return $result;
#    }
#
#    public function payment_requests(){
#        $result = $this->_make_api_call('users/payment_requests');
#        return $result;
#    }
#
#    public function gls_droppoints($params){
#        $result = $this->_make_api_call('shipments/gls_droppoints', false, $params);
#        return $result;
#    }
#
#    public function pdk_droppoints($params){
#        $result = $this->_make_api_call('shipments/pdk_droppoints', false, $params);
#        return $result;
#    }

    #def getToken(self):
    #    return this._token

#    def _make_api_call(method, doPost = False, params = dict()):
#        #$ch = curl_init()
#        urllib.request
#        params['token'] = this._token;
#
#        $query = http_build_query($params);    
#        if doPost:
#            curl_setopt($ch, CURLOPT_URL, self::API_ENDPOINT . '/' . $method);
#            curl_setopt($ch, CURLOPT_POST, 1);
#            curl_setopt($ch, CURLOPT_POSTFIELDS, $query);
#        else:
#            curl_setopt($ch, CURLOPT_URL, self::API_ENDPOINT . '/' . $method . '?' . $query);
#
#        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
#
#        $output = curl_exec ($ch);
#        $http_code = curl_getinfo( $ch, CURLINFO_HTTP_CODE);
#        curl_close ($ch);
#
#        $output = json_decode($output, true);
#
#        if http_code != 200:
#            if(is_array($output['message'])){
#                    print_r($output['message']);
#                    die();
#            }else{
#                    die($output['message']);
#            }
#
#        return output


if __name__ == '__main__':
    pl = Pykkelabels('871684fe-b098-4d04-a96a-527865f162da', '073e628f-c8b6-4911-87b5-63b6fa451fc6')