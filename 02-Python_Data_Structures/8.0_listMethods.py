# Lists 

print('>>> Lists <<<')

"""

alist = ['spam', 'frog', 2.6, 44, [10, 20]]
print('List ', alist)


print('>> Lists are mutable <<')
alist[0] = 'scam'
print(alist)

print('>> Check for item in list <<')
print('Is scam in list: ', 'scam' in alist)
print('Is dog in list: ', 'dog' in alist)

print('>> Loop over list <<')
for item in alist:
   print(item)

print('<<OR>>')

for i in range(len(alist)):
    print(alist[i])

print('>> Concatinate lists <<')
print('alist: ', alist)
blist = ['b', 'c', 'a', 'e', 'd']
print('blist: ', blist)
clist = alist + blist
print(clist)
print('** OR **')
print('>> Extend list <<')
extendlist = alist.extend(blist)
print('Extendlist: ', extendlist)

print('>> Slicing list <<')
print('Start to 4 but not 4: ', clist[:4])
print('From 5 to last: ', clist[5:])
print('From 3 to 7 but not 7: ', clist[3:7])
print('From start to end: ', clist[:])

print('>> Add item to list <<')
clist.append('append')
print('Appended list: ',clist)

print('>> Sort list <<')
print('blist: ', blist)
print('Sorted blist: ', blist.sort())

print('>> Deleting Item from list <<')
# x = list.pop()/ list.pop(index)
print('>Delete with pop()')
print('clist: ', clist)
removedItem = clist.pop()
print('Remove last :', removedItem)
print('clist: ', clist)
removedItem2 = clist.pop(4)
print('Removed inbetween at 4: ', removedItem2)
print('clist: ', clist)

print('>Delete with del')
# del list[start:end]/ list[index]
print('from 1 to 2 but not 2')
del clist[1:2]
print('clist: ',clist)

print('>Delete with remove')
# list.remove('item')
clist.remove('e')
print('clist: ',clist)

numlist = [2,4,5,6,7,5,5,9,0]
print('numlist: ', numlist)
print('>>Find length using len(): ', len(numlist))
print('>>Find max using max(): ', max(numlist))
print('>>Find min using min(): ', min(numlist))
print('>>Find sum using sum(): ', sum(numlist))
print('Calulate average: ', sum(numlist)/len(numlist))

print('>> string and list <<')
string = 'string'
print('String: ', string)
print('String2list: ',list(string))

print('>> Split strings <<')
splitString = 'split-string'
print('String: ', splitString)
spltd = splitString.split('-')
print('Split from - : ', spltd)

print('>> Join string <<')
# says using 'this'.join(list)
print('Join list with space: ', ' '.join(spltd))

# Exercise 1 Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

chList = ['s','e','d','f','v','b','d']
print('chList',chList)

def chop(li):
    li[0] = 'j'
    li[len(li)-1] = 'i'
    print('Modified list:', li)

chop(chList)

def middle(li):
    slis = li[1:len(li)-1]
    return slis

print('Middle: ', middle(chList))

# Exercise 4 Find all unique words and print the list of unique words in alphabetical order. (use text file romeo.txt)

#prompt = 'Enter file name: '
#fileInput = input(prompt)

try:
    fileHandle = open('romeo.txt')
except:
    #print('File can not be opened: ', prompt)
    exit()

wordlist = list()
for line in fileHandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        #print(word)
        if not word in wordlist:
            wordlist.append(word)

wordlist.sort()
print(wordlist)


# Exercise 5 Write a program to read through the mail box data and when you find line that starts with “From”, parse the line and print out the second word, then you will also count the number of From (not From:) lines and print out a count at the end. (use file mbox-short.txt)

fileHandle = open('mbox-short.txt')

count = 0
fromlist = list()
for line in fileHandle:
    if not line.startswith('From '):continue
    line = line.rstrip()
    sline = line.split()
    fromlist.append(sline[1])
    print(sline[1])
    count = count + 1

print('There were',count,'lines in the file with From as the first word')
"""

# Exercise 6 Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

numlist = list()
while True:
    try:
        numInput = input('Enter a number: ')
        if numInput == 'done': break
        number = float(numInput)
        numlist.append(number)
    except:
        print('Invalid Input')
        continue
print('Maximum: ',max(numlist))
print('Minimum: ',min(numlist))



