# Parse eXtensible Markup Language(XML) and JavaScript 
# Object Notation(JSON) received over TCP/IP socket.

# schema for XML - XSD and other
'''
print('>> Parsing eXtensible Markup Language <<')
'''

# XML data received over internet
data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id> 
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>
'''
# stuff is parent to child users, user is parent to child id and child name,
'''
import xml.etree.ElementTree as ET

# Convert data from string to tree node
data = ET.fromstring(data)

# find all user tags under users
users = data.findall('users/user')

# loop-over all user list users
for user in users:
    # find tag name and get the text inside
    print('Name: ',user.find('name').text)
    # get the attribute in tag user
    print('Attribute: ',user.get('x'))

'''
'''
# Parsing JSON(JavaScript Object Notation)
print('>>> Parsing JSON <<<')
print('>> JSON is a form of dictionary. <<')
'''
'''
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
'''
'''
import json

dataObj = json.loads(data)

for user in dataObj:
    print('name : ',user['name'])
    print('id : ',user['id'])

'''
