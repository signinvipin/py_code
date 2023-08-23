# Dictionary
# { 'key':'value' } / { 'key': number } / { number:'key' }
print('>> Dictionary <<')

"""

dictA = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print('dictA: ', dictA)

# create new dictionary
dictNew = dict()
print('New Dictionary: ', dictNew)

# Add pair to dictionary
dictNew['one'] = 1
dictNew['two'] = 2
print('Added pairs: ', dictNew)

# Remove pair from dictionary
del dictNew['two']
print('Removed pair: ', dictNew)

# Retrieve a key's value from dictionary
print('Retrieve value of - one : ', dictNew['one'])

# Retrieve all values in dictionary
print('All values: ', dictA.values())

# Retrieve all values in list form
print('All values in list form: ', list(dictA.values()))

# Make list from dictionary
print('Make list from dictionary: ', list(dictA), '(Only keys)')

# Retrieve all keys from dictionary
print('All keys in list form: ', list(dictA.keys()))

# Retrieve all pairs
print('All pairs: ', list(dictA.items()))

# Check for keys in dictonary
print('Check key one in dictA: ', 'one' in dictA)
print('Check key five in dictA: ', 'five' in dictA)

# Get value of a key using method '.get(key,setDefaultValue)'
print('Get value of two: ', dictA.get('two'))
print('Get value or return default: ', dictA.get('one', 0))

# Looping Dictionary
print('Looping Dictionary')

for key in dictA:
    print('Key: ', key,', Value: ', dictA[key])

print('>> With dict.items() ')
for key,value in dictA.items():
    print('Key: ',key,', Value: ',value)

print('>> Sorting Dictionary in Reverse')
lis =list()
for key in dictA:
    lis.append((dictA[key], key))
# For value based reversed sorting
lis.sort(reversed=True)
print(lis)


# Exercise 2 Write a program that categorizes each mail message by which day of the week the commit was done and keep a running count of each of the days of the week.(use mbox-short.txt)

prompt = 'Enter file name: '
fileInput = input(prompt)
try:
    fileHandle = open(fileInput)
    #fileHandle = open('mbox-short.txt')
except:
    print('File can not be opened: ',fileInput)
    exit()

mailDays = dict()
for line in fileHandle:
    if not line.startswith('From '): continue
    line = line.rstrip()
    splitLine = line.split()
    day = splitLine[2]
    mailDays[day] = mailDays.get(day,0) + 1

print(mailDays)



# Exercise 3 Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary. (use mbox-short.txt)

prompt = 'Enter file name: '
fileInput = input(prompt)

try:
    fileHandle = open(fileInput)
    #fileHandle = open('mbox-short.txt')
except:
    print('File can not be opened: ', fileInput)
    exit()

mailAddress = dict()
for line in fileHandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    address = line[1]
    mailAddress[address] = mailAddress.get(address,0) + 1
    #print(address)

print(mailAddress)



# Exercise 4 Add code to the above program to figure out who has the most messages in the file and print how many messages the person has.(use mbox-short.txt/mbox.txt)


prompt = 'Enter file name: '
fileInput = input(prompt)

try:
    fileHandle = open(fileInput)
    #fileHandle = open('mbox.txt')
except:
    print('File can not be opened: ', fileInput)
    exit()

mailAddress = dict()
for line in fileHandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    address = line[1]
    mailAddress[address] = mailAddress.get(address,0) + 1
    #print(address)

print(mailAddress)

maxKey = None
maxValue = None

for key, value in mailAddress.items():
    if maxKey is None and maxValue is None:
        maxKey = key
        maxValue = value
        continue
    if maxValue < value:
        maxKey = key
        maxValue = value

print(maxKey, maxValue)

"""

# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

prompt = 'Enter file name: '
fileInput = input(prompt)

try:
    fileHandle = open(fileInput)
    #fileHandle = open('mbox-short.txt')
except:
    print('File can not be opened: ', fileInput)
    exit()

mailDomain = dict()
for line in fileHandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    address = line[1]
    address = address.split('@')
    domain = address[1]
    #print(domain)
    mailDomain[domain] = mailDomain.get(domain,0) + 1

print(mailDomain)





















