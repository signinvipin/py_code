# Regular Expression

print('>>> Regular Expression <<<\n')
"""
print('> Special character and character sequences <\n')

print('__ ^ __Matches the beginning of the line.\n')

print('__ $ __Matches the end of the line.\n')

print('__ . __Matches any character (a wildcard).\n')

print('__ \s __Matches a whitespace character.\n')

print('__ \S __Matches a non-whitespace character (opposite of \s).\n')

print('__ * __Applies to the immediately preceding character(s) and indicates to match zero or more times.\n')

print('__ *? __Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.\n')

print('__ + __Applies to the immediately preceding character(s) and indicates to match one or more times.\n')

print('__ +? __Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.\n')

print('__ ? __Applies to the immediately preceding character(s) and indicates to match zero or one time.\n')

print('__ ?? __Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.\n')

print('__ [aeiou] __Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.\n')

print('__ [a-z0-9] __You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.\n')

print('__ [^A-Za-z] __When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.\n')

print('__ ( ) __When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().\n')

print('__ \\b __' ,'Matches the empty string, but only at the start or end of a word.\n')

print('__ \B __Matches the empty string, but not at the start or end of a word.\n')

print('__ \d __Matches any decimal digit; equivalent to the set [0-9].\n')

print('__ \D __Matches any non-digit character; equivalent to the set [^0-9].\n')

# Forming and reading patterns
print('>> Forming and Reading R.E patterns <<')

print('R.E for','From:')
print('__ ^F.+: __')
print('Says, ^ start from F . any character + one or more : have colon.\n')

print('R.E for From: stephen.marquard@uct.ac.za')
print('__ ^F.+:.+@ __')
print('says, after From: any character + one or more @ have at sign\n')

print('R.E. for csev@umich.edu')
print('__ [a-zA-Z0-9]\S+@\S+[a-zA-Z] __')
print('Says, a to z small, A to Z capital, 0 - 9 alphabet or number \S non-whitespace character + one or more @ then have at sign then \S non-whitespace character alphabet small a to z or capital A to Z + one or more\n')

print('R.E for X-DSPAM-Confidence: 0.8475')
print('__ ^X.*: [0-9.]+ __')
print('Says, ^ starts with X . any character zero or more : then have colon and a space [0-9.] any digit including decimal + one or more\n')

print('R.E for hour like 09 in From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008')
print('__ ^F.* ([0-9][0-9]): __')
print('Says, ^ starts with F . any character * zero or more then have space ( start extracting [0-9] [0-9] two digit number ) stop extracting : followed by colon\n')

print('>> R.E for ? Greedy character')
print('Sat Jan  5 09:14:16 2008')

# Search Method
print('Using re.search(pattern, string)')
import re
print('Greedy +/*: ','__ .*  __')
print('Says, . any character * zero or more followed by space')
hour = re.search('.*[0-9]+:','Sat Jan  5 09:14:16 2008')
print('Greedy with re.search: ', hour,'\n')

print('Non-Greedy: ','__ .*?  __')
print('Says, . any character * zero or more non-greedy followed by space')
hourNG = re.search('.*? ', 'Sat Jan  5 09:14:16 2008')
print('Non-Greedy with re.search:', hourNG,'\n')

# Findall Method
print('Using re.findall(pattern, string)')
print('Greedy +/*: ','__ .*  __')
print('Says, . any character * zero or more followed by space')
hour = re.findall('.*[0-9]+:','Sat Jan  5 09:14:16 2008')
print('Greedy with re.findall: ', hour,'\n')

print('Non-Greedy: ','__ .*?  __')
print('Says, . any character * zero or more non-greedy followed by space')
hourNG = re.findall('.*? ', 'Sat Jan  5 09:14:16 2008')
print('Non-Greedy with re.findall:', hourNG,'\n')

# Escape character
print('Escape character \ ')
line = 'I have a $45.00 wrist watch.'
print('Line: ',line)
print('__ \$[0-9.]+\s __')
amt = re.findall('\$[0-9.]+\s', line)
print(amt)

"""

# use of grep (Generalized Regular Expression Parser) for finding in a file on linux os
# $ grep 'pattern' filename

# Example:
# $ grep '^From:' mbox-short.txt

# Exercise 1 Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression.
"""
import re
rePrompt = 'Enter a regular expression: '
reInput = input(rePrompt)

fileHandle = open('mbox.txt')

count = 0
for line in fileHandle:
    find = re.findall(reInput, line)
    if find == []:continue
    count = count + 1

print('mbox.txt had',count,'lines that matched',reInput)
"""

# Exercise 2 Write a program to look for lines of the form: 'New Revision: 39772'. Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.
"""
import re
#prompt = 'Enter file: '
#fileInput = input(prompt)

try:
    #fileHandle = open(fileInput)
    fileHandle = open('mbox.txt')
except:
    #print('File can not be opened',fileInput)
    exit()

numList = list()
for line in fileHandle:
    number = re.findall('^N.*: ([0-9]+)',line)
    if number == []: continue
    #print(number)
    numList.append(int(number[0]))

print('Average: ',int(sum(numList)/len(numList)))
"""














