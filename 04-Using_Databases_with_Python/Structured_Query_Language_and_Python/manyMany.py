## Create Many to Many Database Type


import sqlite3

try:
    connDb = sqlite3.connect('manyMany.db3')
    cursorActive = connDb.cursor()

    cursorActive.execute('DROP TABLE IF EXISTS roles')
    cursorActive.execute('DROP TABLE IF EXISTS users')
    cursorActive.execute('DROP TABLE IF EXISTS courses')
    cursorActive.execute('DROP TABLE IF EXISTS members')


    cursorActive.execute(''' CREATE TABLE users(
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    )''')

    cursorActive.execute(''' CREATE TABLE roles (
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        role TEXT UNIQUE
    )''')

    cursorActive.execute(''' CREATE TABLE courses (
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    )''')

    cursorActive.execute(''' CREATE TABLE members (
        name_id    INTEGER,
        title_id   INTEGER,
        role_id    INTEGER,
                   PRIMARY KEY('name_id','title_id')
    )''')


    cursorActive.execute(''' INSERT OR IGNORE INTO users (name) VALUES (?)''',('John',))
    cursorActive.execute(''' INSERT OR IGNORE INTO users (name) VALUES (?)''',('Joe',))
    cursorActive.execute(''' INSERT OR IGNORE INTO users (name) VALUES (?)''',('Sally',))
    cursorActive.execute(''' INSERT OR IGNORE INTO users (name) VALUES (?)''',('Mike',))
    cursorActive.execute(''' INSERT OR IGNORE INTO users (name) VALUES (?)''',('Rakesh',))
    cursorActive.execute(''' INSERT OR IGNORE INTO users (name) VALUES (?)''',('Gita',))

    cursorActive.execute(''' INSERT OR IGNORE INTO courses (title) VALUES (?)''',('HTML',))
    cursorActive.execute(''' INSERT OR IGNORE INTO courses (title) VALUES (?)''',('Python',))
    cursorActive.execute(''' INSERT OR IGNORE INTO courses (title) VALUES (?)''',('SQL',))
    cursorActive.execute(''' INSERT OR IGNORE INTO courses (title) VALUES (?)''',('PHP',))

    cursorActive.execute(''' INSERT OR IGNORE INTO roles (role) VALUES (?)''',('Instructor',))
    cursorActive.execute(''' INSERT OR IGNORE INTO roles (role) VALUES (?)''',('Student',))

    cursorActive.execute(''' INSERT OR REPLACE INTO members (name_id, title_id, role_id) VALUES (?,?,?)''',(1,2,1))
    cursorActive.execute(''' INSERT OR REPLACE INTO members (name_id, title_id, role_id) VALUES (?,?,?)''',(4,2,2))
    cursorActive.execute(''' INSERT OR REPLACE INTO members (name_id, title_id, role_id) VALUES (?,?,?)''',(5,2,1))
    cursorActive.execute(''' INSERT OR REPLACE INTO members (name_id, title_id, role_id) VALUES (?,?,?)''',(3,3,2))
    cursorActive.execute(''' INSERT OR REPLACE INTO members (name_id, title_id, role_id) VALUES (?,?,?)''',(2,4,1))
    cursorActive.execute(''' INSERT OR REPLACE INTO members (name_id, title_id, role_id) VALUES (?,?,?)''',(6,3,2))

    dataRetrieved = cursorActive.execute(''' SELECT users.name, courses.title, roles.role 
        FROM members JOIN roles JOIN users JOIN courses 
        ON members.role_id = roles.id AND members.name_id = users.id AND members.title_id = courses.id 
        ORDER BY users.name ASC, courses.title, roles.role ''')

    for name, title, role in dataRetrieved:
        print('name: ',name,', title: ',title,', role: ', role)


    connDb.commit()
    cursorActive.close()

except Exception as err:
    tb = err.__traceback__
    print('Error:',err,', at line',tb.tb_lineno)

