# Accessing Networked Data Using Python

print('>>> Access Networked Data <<<\n')

print('> Simple Web Browser <\n')

## Using socket library to create connection
# pc > internet --- internet > pc > socket > port > application

# Import socket library
# socket provide port to connect to application
# print('> Using Socket library <')

"""

print('**For Text/Plain**\n')

import socket

# Create socket
appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
appSocket.connect(('data.pr4e.org',80))

# Send encoded GET request 
# use encode() or byte string, b'' to encode
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
appSocket.send(request)

# Recieve data in packets
while True:
    data = appSocket.recv(5120)
    if len(data) < 1: break
    print(data.decode(), end='')

# Close the socket connection
appSocket.close()
"""
"""
print('**For image/jpeg**\n')
# Imported library socket
# Import library time
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
imgSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
imgSocket.connect((HOST,PORT))

# send request using sendall() for byte string enoding
request = b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'
imgSocket.sendall(request)

lengthTotal = 0
picture = b""
while True:
    data = imgSocket.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    lengthTotal = lengthTotal + len(data)
    print(lengthTotal, len(data))
    picture = picture + data

#print(picture)
imgSocket.close()

# Remove and print header
# 'wb' write byte mode
pos = picture.find(b"\r\n\r\n")
print('Header length',pos)
print('Header',picture[:pos].decode())

# Save data to image
picture = picture[pos+4:]

img = open("requestedImage.jpg", "wb")
img.write(picture)
img.close()

"""

## Using urllib library to make request
print('>> Using urllib library <<')
# urllib.request
# urllib.parse
# urllib.error

"""
print('For plain/text')

# import library
import urllib.request, urllib.parse, urllib.error

# try catch errors
try:
    # request url and get data
    fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    # loop over data and read/decode it
    for line in fileHandle:
        # decode() with text file
        print(line.decode(),end='')
except Exception as err :
    print('Error:',err)
"""

print('For image/jpeg')
# size of data package recieved is auto for small byte strings
"""
import urllib.request, urllib.parse, urllib.error

try:
    # request and get picture bytes
    picture = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
    # read/decode bytes
    picture = picture.read()
    # open a image file to be written
    imageHandle = open('requestedImage2.jpg','wb')
    # write data to image file
    imageHandle.write(picture)
    # close image file
    imageHandle.close()
    print('Operation complete! You can view the image.')
except Exception as err:
    print('Error:',err)
"""
"""
# set the data package recieved size manually
import urllib.request, urllib.parse, urllib.error

try:
    picData = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

    imgHandle = open('requestedImage2.jpg','wb')
    picture = b""
    length = 0
    while True:
        # set packet size manually
        data = picData.read(102400)
        if len(data) < 1: break
        length = length + len(data)
        picture = picture + data
        # write the data to file, before getting new
        # this clears the memory for next data
        imgHandle.write(picture)
        imgHandle.close()

        # can raise exception
        #if (!picture)raise Exception('Ohoo! why this error.')

    print('Yay! Operation complete. File can be viewed.')
except Exception as err:
    print('Error: ',err.reason)
"""

# Code to use on linux systems to get files
"""
import os
import urllib.request, urllib.parse, urllib.error

print('Please enter a URL like http://data.pr4e.org/cover3.jpg')
urlstr = input().strip()
img = urllib.request.urlopen(urlstr)

# Get the last "word"
words = urlstr.split('/')
fname = words[-1]

# Don't overwrite the file
if os.path.exists(fname):
    if input('Replace ' + fname + ' (Y/n)?') != 'Y':
        print('Data not copied')
        exit()
    print('Replacing', fname)

fhand = open(fname, 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied to', fname)
fhand.close()

"""
















