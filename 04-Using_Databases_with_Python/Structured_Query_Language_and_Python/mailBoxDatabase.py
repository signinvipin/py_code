# Create table having emails and counts,
# use text file input.

#GitHub\py_code\02-Python_Data_Structures

import sqlite3
import re

try:
    #prompt = 'Enter file name: '
    #fileInput = input(prompt)
    #fileHandle = open(fileInput)
    fileHandle = open('./../../02-Python_Data_Structures/mbox.txt')

    dbConnect = sqlite3.connect('dbEmail.sqlite3')
    actCursor = dbConnect.cursor()

    actCursor.execute('DROP TABLE IF EXISTS mboxData')

    actCursor.execute(''' CREATE TABLE 'mboxData' (
        email   TEXT,
        count   INTEGER
    )''')


    mail = ''
    for line in fileHandle:
        mailFrom = re.findall('^F.*: (\S*@\S*)',line)
        if len(mailFrom) < 1: continue
        mail = mailFrom[0]
        present = actCursor.execute(''' SELECT count FROM mboxData WHERE email = ? ''', (mail,))
        row = present.fetchone()
        #print('mail',mail,'row:',row)

        if row == None:
            actCursor.execute(''' INSERT INTO mboxData (email, count) VALUES (?,?) ''', (mail, 1))
        else:
            actCursor.execute(''' UPDATE mboxData SET count = count + 1 WHERE email = ? ''', (mail,))

    readData = actCursor.execute('SELECT * FROM mboxData')
    for row in readData:
        print('Email:',row[0],', Counts:',row[1])

    dbConnect.commit()
    dbConnect.close()

except Exception as err:
    trc = err.__traceback__
    print('Error:',err,'at line',trc.tb_lineno)


