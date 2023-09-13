## Create one to many relational table database


import sqlite3

try:
    connection = sqlite3.connect('oneMany.sqlite3')
    cursorActive = connection.cursor()

    cursorActive.execute('DROP TABLE IF EXISTS students')
    cursorActive.execute('DROP TABLE IF EXISTS subjects')
    cursorActive.execute('DROP TABLE IF EXISTS class')

    cursorActive.execute(''' CREATE TABLE students(
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT
    ) ''')

    cursorActive.execute(''' CREATE TABLE subjects(
        id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        subject  TEXT
    )''')

    cursorActive.execute(''' CREATE TABLE class(
        student_id INTEGER,
        subject_id INTEGER
    ) ''')

    cursorActive.execute(''' INSERT INTO students (name) VALUES (?)''',('Akash',))
    cursorActive.execute(''' INSERT INTO students (name) VALUES (?)''',('Nitin',))
    cursorActive.execute(''' INSERT INTO students (name) VALUES (?)''',('Sanjay',))
    cursorActive.execute(''' INSERT INTO students (name) VALUES (?)''',('John',))
    cursorActive.execute(''' INSERT INTO students (name) VALUES (?)''',('Sally',))

    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Math',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Science',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Geography',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('History',))
    cursorActive.execute(''' INSERT INTO subjects (subject) VALUES (?)''',('Civics',))

    cursorActive.execute(''' INSERT INTO class (student_id, subject_id) VALUES (?,?)''',(1,2))
    cursorActive.execute(''' INSERT INTO class (student_id, subject_id) VALUES (?,?)''',(4,2))
    cursorActive.execute(''' INSERT INTO class (student_id, subject_id) VALUES (?,?)''',(2,5))
    cursorActive.execute(''' INSERT INTO class (student_id, subject_id) VALUES (?,?)''',(3,4))
    cursorActive.execute(''' INSERT INTO class (student_id, subject_id) VALUES (?,?)''',(5,1))

    classData = cursorActive.execute(''' SELECT students.name, subjects.subject FROM class JOIN students JOIN 
subjects ON class.student_id = students.id AND class.subject_id = subjects.id ''')

    connection.commit()

    for name,subject in classData:
        print(name, subject)

    cursorActive.close()


except Exception as err:
    tb = err.__traceback__
    print('Error:',err,', at line',tb.tb_lineno)
