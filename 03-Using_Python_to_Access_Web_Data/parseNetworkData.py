## Parsing Web Pages 
# Creating web crawler which parses the web pages.

"""
print('>> Parsing web pages using urllib and RegEx. <<\n')

try:
    import urllib.request, urllib.parse, urllib.error
    import re
    import ssl

    # Create context for https verification override
    ctx = ssl.create_default_context()
    ctx.hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL: ')
    #url = 'https://docs.python.org'
    # Read returns whole webpage as a big string
    pageData = urllib.request.urlopen(url, context = ctx).read()
    links = re.findall(b'"(http[s]?://.+?)"',pageData)
    for link in links:
        print(link.decode())

except Exception as err:
    tracebackObj = err.__traceback__
    print('Error:',str(err)+', ln',tracebackObj.tb_lineno)
"""
"""
print('>> Webpage parsing with Beautiful Soup 4 <<')
try:
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Creating context to pass/skip https ssl verification
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #url = input('Enter URL: ')
    url = 'https://docs.python.org'

    # read all the data and return a string
    pageData = urllib.request.urlopen(url, context = ctx).read()

    # parse the data using python html.parser
    # to use different parser, visit beautiful soup site
    soup = BeautifulSoup(pageData,'html.parser')

    #Retrieve Data, parse links from webpages
    tags = soup('a')
    for tag in tags:
        print(tag['href'])

except Exception as err:
    tbObject = err.__traceback__
    print('Error: ',str(err)+',ln',tbObject.tb_lineno)

"""

## On linux systems curl(copyURL) and wget are similar to urllib
# $ curl -O http://www.py4e.com/cover.jpg
# $ wget http://www.py4e.com/cover.jpg













