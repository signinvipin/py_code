# Tuples

# tuple('string')
# 'a', - with end comma it's a tuple
# t = ('a',) type=tuple

print('>> Tuple : immutable sequence of values separated by commas')
"""
#Creating tuple
creat = tuple('cage')
print('Tuple: ',creat)


t = 'g', 'f', 'e', 'h', 'c', 'b', 'a', 'd'
print('Tuple - t: ', t)

# type
print('type of t: ', type(t))

# slice tuple
print('Slicing begin to middle: ',t[:4])

# Retrieving Value
print('Get value at 4: ', t[4])

# Adding to tuples
print('Adding two tuples: ', t + ('i',))

# Tuple assignment and Flipping values
var = ['cat','dog']
print('List: ',var)

(A, B) = var
print('A: ', A, 'B: ', B)

(B, A) = (A, B)
print('Flipping Values, A: ',A,'B: ',B) 

# Comparing tuples
abb = ('c','a','t')
bcc = ('c','a','r')

print('Compare, abb: ',abb,' and bcc: ',bcc)
print('Is abb > bcc? ', abb > bcc)
print('Is bcc == abb? ',bcc == abb)

# Exercise 1 Read and parse the “From” lines and pull out the addresses. Count the number of messages from each person using a dictionary. After, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

prompt = 'Enter file name: '
fileInput = input(prompt)

try:
    fileHandle = open(fileInput)
    #fileHandle = open('mbox-short.txt')
except:
    print('File can not be opened: ',fileInput)
    exit()

dictAdd = dict()
for line in fileHandle:
    if not line.startswith('From '): continue
    line = line.rstrip()
    line = line.split()
    add = line[1]
    #print(add)
    dictAdd[add] = dictAdd.get(add,0) + 1

#print(dictAdd)
#sorting in reverse
listAdd = list()
for key in dictAdd:
    listAdd.append((dictAdd[key], key))

listAdd.sort(reverse = True)
(count, address) = listAdd[0]
print('Address:',address,', with commits:',count)


# Exercise 2  This program counts the distribution of the hour of the day for each of the messages.Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour.(use mbox-short.txt)

prompt = 'Enter file name: '
fileInput = input(prompt)

try:
    fileHandle = open(fileInput)
    #fileHandle = open('mbox-short.txt')
except:
    print('File can not be opened: ',fileInput)
    exit()

dictHour = dict()
for line in fileHandle:
    if not line.startswith('From '): continue
    line = line.rstrip()
    line = line.split()
    time = line[5]
    time = time.split(':')
    hour = time[0]
    #print(hour)
    dictHour[hour] = dictHour.get(hour,0) + 1

#print(dictHour)

#sorting in reverse
listHour = list()
for hour in dictHour:
    listHour.append((hour, dictHour[hour]))

listHour.sort()
for hour, number in listHour:
    print('Hour:',hour,', with commits:',number)

"""


























