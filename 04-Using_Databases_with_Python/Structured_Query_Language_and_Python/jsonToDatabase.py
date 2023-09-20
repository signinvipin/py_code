## Create a relational database from json file data

import sqlite3
import json

try:
    conn = sqlite3.connect('jsonToDatabase.sqlite3')
    cursorAct = conn.cursor()

    cursorAct.executescript(''' 
    DROP TABLE IF EXISTS roles;
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS members;

    CREATE TABLE roles (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        role  TEXT UNIQUE
    );

    CREATE TABLE users (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT UNIQUE
    );

    CREATE TABLE courses (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE members (
        user_id   INTEGER,
        course_id  INTEGER,
        role_id    INTEGER, PRIMARY KEY(user_id, course_id)
    );

    INSERT OR IGNORE INTO roles(role) VALUES ('STUDENT');
    INSERT OR IGNORE INTO roles(role) VALUES ('INSTRUCTOR');

    ''')

    prompt = 'Enter file name: '
    fileName = input(prompt)

    if len(fileName) < 1 : fileName = 'roster_data_sample.json'

    data = open(fileName).read()
    jsonData = json.loads(data)

    for name, title, role in jsonData:
        role = role + 1
        #print(name, course, role)

        cursorAct.execute(''' INSERT OR IGNORE INTO users(name) VALUES (?)''',(name,))
        users_id = cursorAct.execute(''' SELECT id FROM users WHERE name = (?) ''',(name,)).fetchone()[0]

        cursorAct.execute(''' INSERT OR IGNORE INTO courses(title) VALUES (?) ''',(title,))
        courses_id = cursorAct.execute(''' SELECT id FROM courses WHERE title = (?) ''',(title,)).fetchone()[0]

        #print('users_id:',users_id,' courses_id:',courses_id,' role:',role)

        cursorAct.execute('''INSERT OR REPLACE INTO members(user_id, course_id, role_id) VALUES (?,?,?)''',(users_id, courses_id, role))
        

        conn.commit()

    #data = cursorAct.execute(''' SELECT users.name, 
    #courses.title, roles.role FROM members JOIN users 
    #JOIN courses JOIN roles ON members.user_id = 
    #users.id AND members.course_id = courses.id AND 
    #members.role_id = roles.id ORDER BY users.name ASC, 
    #courses.title, roles.role ''')

    #cursorAct.close()


except Exception as err:
    tb = err.__traceback__
    print('Error:',err,', at line',tb.tb_lineno)

