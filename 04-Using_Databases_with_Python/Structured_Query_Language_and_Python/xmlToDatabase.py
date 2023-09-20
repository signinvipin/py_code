## Create a relational database from xml file data

import sqlite3
import xml.etree.ElementTree as et

try:
    conn = sqlite3.connect('xmlToDatabase.sqlite3')
    cursorAct = conn.cursor()

    cursorAct.executescript(''' 
    DROP TABLE IF EXISTS Artists;
    DROP TABLE IF EXISTS Albums;
    DROP TABLE IF EXISTS Tracks;

    CREATE TABLE Artists (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist  TEXT UNIQUE
    );

    CREATE TABLE Albums (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        album  TEXT UNIQUE
    );

    CREATE TABLE Tracks (
        id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title    TEXT UNIQUE,
        album_id INTEGER,
        len      INTEGER,
        rating   INTEGER,
        count    INTEGER
    );

    ''')

    prompt = 'Enter file name: '
    fileName = input(prompt)

    if len(fileName) < 1 : fileName = 'Library.xml'

    data = open(fileName)
    xmlData = et.parse(data)
    #print(xmlData)
    allDicts = xmlData.findall('dict/dict/dict')
    #print('allDicts created')

    def ifPresent(data,key):
        #print(data.tag, key)
        found = False
        for child in data:
            if found : return child.text
            if child.tag == 'key' and child.text == key:
                found = True
        #print('None')
        return None

    for dict in allDicts:
        #print('dict loop started')
        if (ifPresent(dict, 'Track ID') is None): continue

        name   = ifPresent(dict, 'Name')
        artist = ifPresent(dict, 'Artist')
        album  = ifPresent(dict, 'Album')
        count  = ifPresent(dict, 'Play Count')
        rating = ifPresent(dict, 'Rating')
        length = ifPresent(dict, 'Total Time')

        if name is None or artist is None or album is None: continue

        #print('Name:',name,'Artist:',artist,'Album:',album,'Count:',count,'Rating:', rating,'Length:', length)


        cursorAct.execute(''' INSERT OR IGNORE INTO artists(artist) VALUES (?)''',(artist,))
        artist_id = cursorAct.execute(''' SELECT id FROM artists WHERE artist = (?) ''',(artist,)).fetchone()[0]

        cursorAct.execute(''' INSERT OR IGNORE INTO albums(artist_id, album) VALUES (?,?) ''',(artist_id, album))
        album_id = cursorAct.execute(''' SELECT id FROM albums WHERE album = (?) ''',(album,)).fetchone()[0]

        #print('artist_id:',artist_id,' album_id:',album_id)

        cursorAct.execute('''INSERT OR REPLACE INTO Tracks(title, album_id, len, rating, count) VALUES (?,?,?,?,?)''',(name, 
album_id, length, rating, count))

        conn.commit()

    data = cursorAct.execute(''' SELECT Tracks.title, Albums.album, Artists.artist, Tracks.len, Tracks.rating, Tracks.count
         FROM Tracks JOIN Albums JOIN Artists 
         ON Tracks.album_id = Albums.id AND Albums.artist_id = Artists.id
         ORDER BY Tracks.title, Albums.album, Artists.artist ''')

    for title,artist,album,count,rating,length in data:
        print('Name:',title,', Artist:',artist,', Album:',album,', Count:',count,', Rating:', rating,', Length:', length)

    conn.commit()
    cursorAct.close()


except Exception as err:
    tb = err.__traceback__
    print('Error:',err,', at line',tb.tb_lineno)

