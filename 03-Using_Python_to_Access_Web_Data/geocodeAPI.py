## Google Geocoding API 
# Enter improper address and get geoposition with proper address

print('>>> Google GeoCoding <<<')

'''
print('>> Geocoding with json format <<')

import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

try:
    while True:
        prompt = 'Enter address: '
        addressInput = input(prompt)
        if len(addressInput) < 1:
            raise Exception('**Invalid Input**')
            #break

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        urlEncode = urllib.parse.urlencode({'address':addressInput, 'key': api_key})
        requestUrl = serviceurl + urlEncode

        print('Retrieving :',requestUrl)
        requestData = urllib.request.urlopen(requestUrl, context=ctx)
        receivedData = requestData.read().decode()
        print('Received',len(receivedData),'characters.')

        jsonData = json.loads(receivedData)

        if not jsonData: jsonData = None

        # Check for jsonData
        if jsonData == None or 'status' not in jsonData or jsonData['status'] != "OK":
            print('** Problem retrieving data. Try again! **')
            print(jsonData)
            continue

        # Dumps the data received to display
        print(json.dumps(jsonData, indent=4))

        lat =jsonData['results'][0]['geometry']['location']['lat']
        lng = jsonData['results'][0]['geometry']['location']['lng']

        print('Address: ',jsonData['results'][0]['formatted_address'])
        print('Lat:',lat,'Lng:',lng)

except Exception as err:
    traceObject = err.__traceback__
    print('Error :',err,'at line',traceObject.tb_lineno)
'''

'''
print('>> Geocoding with xml')

import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as et

api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

try:
    while True:
        prompt = 'Enter address: '
        addressInput = input(prompt)
        if len(addressInput) < 1:
            raise Exception('**Invalid Input**')
            #break

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        urlEncode = urllib.parse.urlencode({'address':addressInput, 'key': api_key})
        requestUrl = serviceurl + urlEncode

        print('Retrieving :',requestUrl)
        requestData = urllib.request.urlopen(requestUrl, context=ctx)
        receivedData = requestData.read().decode()
        print('Received',len(receivedData),'characters.')

        xmlData = et.fromstring(receivedData)

        if not xmlData: xmlData = None

        # Check for jsonData
        if xmlData == None or xmlData.find('status') or xmlData.find('status').text != "OK":
            print('** Problem retrieving data. Try again! **')
            print(xmlData)
            continue

        # Dumps the data received to display
        print(receivedData)

        # level-down through nodes in tree to find
        lat = xmlData.find('result').find('geometry').find('location').find('lat').text
        lng = xmlData.find('result').find('geometry').find('location').find('lat').text

        print('Address: ', xmlData.find('result').find('formatted_address').text)
        print('Lat:',lat,'Lng:',lng)


except Exception as err:
    traceObject = err.__traceback__
    print('Error :',err,'at line',traceObject.tb_lineno)

'''
