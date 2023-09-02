### Structured Query Language (SQL)

# Use DBBrowser to create database and CRUD database content

>> Creating Database

CREATE TABLE 'users'(
    name  VARCHAR(128),
    email VARCHAR(128)
)

# 'users' represents the table-name
# name and email will be the column names to be created
# VARCHAR(128) represents type and count of characters allowed as value  

..CRUD..

>> Creating entries

INSERT INTO users (name, email) VALUES ('Sanjay', 'sanjay@amity.edu')

# name and email not in quotes represents columns
# values in quoted strings are the values to respective columns 

>> Reading entries

SELECT * FROM users
# * selects and returns all entries from table

SELECT email WHERE name = 'Sanjay'
# selects and returns a particular entry after checking provided condition

>> Updating entries

UPDATE users SET name = 'SanjayKumar' WHERE name = 'Sanjay'
# selects and changes values upon passing condition

>> Deleting entries

DELETE FROM users WHERE name = 'SanjayKumar'
# selects and deletes row upon passing condition

# click 'Execute' after typing any command to implement
