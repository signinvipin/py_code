## Create one to many relational table database


import sqlite3

try:
    connection = sqlite3.connect('oneMany.sqlite3')
    cursorActive = connection.cursor()

    cursorActive.execute('DROP TABLE IF EXISTS students')
    cursorActive.execute('DROP TABLE IF EXISTS subjects')

    cursorActive.execute(''' CREATE TABLE subjects(
        id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        subject  TEXT
    )''')

    cursorActive.execute(''' CREATE TABLE students(
        id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name       TEXT,
        subject_id INTEGER
    ) ''')

    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Math',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Science',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Geography',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('History',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Civics',))

    cursorActive.execute(''' INSERT INTO students (name, subject_id) VALUES (?,?)''',('Akash',2))
    cursorActive.execute(''' INSERT INTO students (name, subject_id) VALUES (?,?)''',('Nitin',2))
    cursorActive.execute(''' INSERT INTO students (name, subject_id) VALUES (?,?)''',('Sanjay',1))
    cursorActive.execute(''' INSERT INTO students (name, subject_id) VALUES (?,?)''',('John',3))
    cursorActive.execute(''' INSERT INTO students (name, subject_id) VALUES (?,?)''',('Sally',4))

    classData = cursorActive.execute(''' SELECT students.name, subjects.subject FROM students JOIN 
subjects ON students.subject_id = subjects.id ''')

    connection.commit()

    for name,subject in classData:
        print(name, subject)

    cursorActive.close()


except Exception as err:
    tb = err.__traceback__
    print('Error:',err,', at line',tb.tb_lineno)
