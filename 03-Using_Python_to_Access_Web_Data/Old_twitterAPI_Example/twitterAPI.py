## TwitterAPI

#For the programs we run with Twitter, 
#we hide all the complexity in the files oauth.py and twurl.py.
#We simply set the secrets in hidden.py and then send the 
#desired URL to the twurl.augment() function and 
#the library code adds all the necessary parameters to the 
#URL for us.

#Twitter-1 This program retrieves the timeline for a 
#particular Twitter user
#and returns it to us in JSON format in a string. 
#We simply print the first 250 characters of the string.

'''
import urllib.request, urllib.parse, urllib.error
import twitterURL
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twitterURL.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    # print headers, informs no. of requests left
    print('Remaining', headers['x-rate-limit-remaining'])

'''

## Twitter-2 To retrieve a user’s Twitter friends, 
# parse the returned JSON, and extract some of the information 
# Also dump the JSON after parsing and 
# “pretty-print” it with an indent of four characters to allow us
# to pore through the data when we want to extract more fields.

'''
import urllib.request, urllib.parse, urllib.error
import twitterURL
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twitterURL.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
'''
