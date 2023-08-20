# Files

## >> Reading Files
# Opening Files
fileName = input('Enter file name: ')

# Catch file input errors
try:
    # fileHandle returns the string blob
    ## open('fileName',optional-'r'/'w')
    fileHandle = open(fileName)
except:
    print('File can not be opened:', fileName)
    exit()   # terminates the program

## Read file once only as it exhauts the source
#reads = fileHandle.read()
#print(fileName,'reads',reads)

# Looping through file data
count = 0
for line in fileHandle:
    # strip all whitespaces
    line = line.rstrip()
    if line.startswith('From:'):
    # if line.find('@') == -1: continue
    # if not line.startswith('From:'): continue
        print(line)
        count = count + 1
print('There were',count,'from lines in',fileName) 



## >> Writing Files

# Open file
file = open('writeFile.txt', 'w')
line1 = 'This is first line in file.\n'

# add string to file
file.write(line1)

# can add more lines
line2 = 'This is second line.\n'
file.write(line2)

# Close the file
file.close()

## >> Exercises

# Exerise 1 Write a program to read through a file and print the contents of the file (line by line) all in upper case. (use file mbox-short.txt)
print('>>> Exercise 1 <<<')
fileInput = input('Enter file name:')

try:
    fileHandle = open(fileInput)
except:
    print('File can not be opened: ',fileInput)

for line in fileHandle:
    line = line.upper()
    print(line)


# Exercise 2 Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.Test your file on the mbox.txt and mbox-short.txt files.
print('>>> Exercise 2 <<<')
import re
fileInput = input('Enter file name: ')

try:
    fileHandle = open(fileInput)
except:
    print('File can not be opened: ',fileInput)

count = 0
total = 0
for line in fileHandle:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence'):continue
    count = count + 1
    index = line.find(':')
    value = line[index+1:]
    total = total + float(value)
print('Average spam confidence: ',total/count)















