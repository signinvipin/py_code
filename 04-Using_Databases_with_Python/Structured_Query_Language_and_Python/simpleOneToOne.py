# Create table having emails and counts,
# use text file input.

#GitHub\py_code\02-Python_Data_Structures

import sqlite3
import re

try:
    prompt = 'Enter file name: '
    fileInput = input(prompt)

    # Auto select file upon hitting enter
    if len(fileInput) < 1: fileInput = './../../02-Python_Data_Structures/mbox.txt'

    fileHandle = open(fileInput)

    # Create or open database file
    dbConnect = sqlite3.connect('dbEmail.sqlite3')
    # Activate Cursor for command execution
    actCursor = dbConnect.cursor()

    # Execute SQL commands
    # Drop pre-existing table if any
    actCursor.execute('DROP TABLE IF EXISTS mboxData')

    # Create new table in database
    actCursor.execute(''' CREATE TABLE 'mboxData' (
        email   TEXT,
        count   INTEGER
    )''')

    # Retreive data to be entered in table
    for line in fileHandle:
        mailFrom = re.findall('^F.*: (\S*@\S*)',line)
        if len(mailFrom) < 1: continue
        mail = mailFrom[0]

        # Search table if entry exists
        present = actCursor.execute(''' SELECT count FROM mboxData WHERE email = ? ''', (mail,))

        # Get an entry if exist
        row = present.fetchone()
        #print('mail',mail,'row:',row)

        if row == None:
            # Insert entry and value to table row
            actCursor.execute(''' INSERT INTO mboxData (email, count) VALUES (?,?) ''', (mail, 1))
        else:
            # Change and update value to entry
            actCursor.execute(''' UPDATE mboxData SET count = count + 1 WHERE email = ? ''', (mail,))

    # Read the table from database for top 5 readings
    readData = actCursor.execute('SELECT * FROM mboxData ORDER BY count DESC LIMIT 5')
    for row in readData:
        print('Email:',row[0],', Counts:',row[1])

    # Commit to the connection all the changes made
    dbConnect.commit()

    # Close the connection
    dbConnect.close()

except Exception as err:
    trc = err.__traceback__
    print('Error:',err,'at line',trc.tb_lineno)


