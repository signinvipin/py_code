# Strings
print('>>Strings')

fruit = 'banana'
# string in quotes

# retrieving character from string
print('>String: '+fruit+', indexed from 0 to 5')
print('Retrieving third letter: '+fruit[2])
print('Retrieving first letter: '+fruit[0])

# Getting length of string
print(">>Getting length of string using 'len'.")
## len('string') 
length = len(fruit)
print('Length of fruit: '+str(length))

# Getting the last letter
print('>>Getting the last letter of string')
last = fruit[length - 1]
orlast = fruit[-1]
print('Last with length: '+last+', or Last with negative indices: '+orlast)

# Looping through the loop - traversing
# while loop
print('>>Looping String')
print('>Using indefinite while-loop')
index = 0
while index < length:
    letter = fruit[index]
    print(letter)
    index = index + 1

# for loop
print('>Using definite for-loop')
for letter in fruit:
    print(letter)

# Exercise-1_Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
print('>>Looping String in Reverse')
index = -1
while index > -length:
    letter = fruit[index]
    print(letter)
    index = index - 1

# Slicing String
print('>>Slicing String')
strg = 'black goat'
print('String: '+strg)

# All from start upto 3 but not letter at 3
print(strg[:3])

# From 4 all towards end
print(strg[4:])

# From 3 upto 8 but not 8
print(strg[3:8])

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# It means all from start to end
print(strg[:])

# Immutable Strings
print('>>Strings are immutable, cannot be changed using bracket notation')

# Change string
print('>>Mutate string by creating new from slicing and adding to old')
greeting = 'Hello'
print(greeting)
newGreeting = 'Y'+greeting[1:]+'w'
print(newGreeting)

# Looping and Counting
print('>>Looping String and Counting letter appearance')

word = 'banana'
print('Word : '+word)
counter = 0
for letter in word:
    if letter != 'a': continue
    counter = counter + 1
print('Letter-a count: '+str(counter))

#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# Count letter function
print('>>Count letter function')
word = 'catalogue'
letter = 's'
print("Count "+letter+" in word: "+word)

def countLetter(strng, letter):
    count = 0
    for ltr in strng:
        if ltr == letter:
            count = count + 1
    print('Word '+word+' has '+str(count)+' letter '+letter+' in it.')

countLetter(word, letter)

# Check for letter in word using 'in' operator
print(">>Check for letter using 'in' operator")
print("Check for 'i' in word 'bike'")
print('i' in 'bike')
print("Check for 'a' in word 'bike'")
print('a' in 'bike')

# String Methods
print('>>Methods that can be applied to strings')
strOne = 'bicycle'
print('bicycle')
dir(strOne)

# Calling methods on string
print('>>Calling method on string')
word = 'bicycle'
capWord = word.upper()
print('UpperCase: '+capWord)

# Find a letter in string
# .find(string) or .find(string, startPosition)
index = word.find('c')
print(">Find 'c': "+str(index))

index = word.find('c', 3)
print(">Find second 'c': "+str(index))

# Remove whitespaces
line = '  here I come  '
print('Line :'+line)
newLine = line.strip()
print('NewLine :'+newLine)

# Check string starts with
print('>>Check startswith')
line = 'here we go'
print(line)
check = line.startswith('h')
print("Line starts with 'h': "+str(check))

# Exercise 4. Write an invocation that counts the number of times the letter a occurs in “banana”.
# Count a letter in string
word = 'banana'
print(word)
print(">>Count letter 'a'")
count = word.count('a')
print('Count is: '+str(count))

# Format operator %
# %d - digits , %g - floats, %s - strings
goats = 55
print('>>I have spotted %d goats in open.' % goats)

# Exercise 5 - Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
strTwo = 'X-DSPAM-Confidence:0.8475'

index = strTwo.find(':')
extract = strTwo[index+1:]
print(float(extract))





















