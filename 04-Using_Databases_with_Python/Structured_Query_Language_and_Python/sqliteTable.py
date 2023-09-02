## Create database and table using SQL in python

try:
    import sqlite3

    con = sqlite3.connect('sqliteNew.db')
    cursorHandle = con.cursor()

    cursorHandle.execute('''DROP TABLE IF EXISTS users ''')

    cursorHandle.execute(''' 
        CREATE TABLE 'users' (
            name   VARCHAR(128),
            email  VARCHAR(128)
    ) ''')


    cursorHandle.execute('''INSERT INTO users (name, email) 
        VALUES (?,?)''', ('Rohit', 'rohit@amity.edu'))

    con.commit()

    read = cursorHandle.execute(''' SELECT * FROM users ''')

    # Use fetchone() when selecting single row
    #print(read.fetchone())

    for data in read:
        print(data)

    cursorHandle.close()

except Exception as err:
    trc = err.__traceback__
    print('Error:',err,'at line',trc.tb_lineno)
