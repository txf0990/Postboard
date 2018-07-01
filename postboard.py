#!/usr/bin/env python
import sqlite3

class Database(object):
    'this is the database.'
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS board(ID integer PRIMARY KEY AUTOINCREMENT, content text)")
    def addEntry(self, entry):
        self.c.execute("INSERT INTO board(content) Values(?)", (entry,))
        self.conn.commit()
    def deleteEntry(self, ID):
        self.c.execute("DELETE FROM board WHERE ID=?", (ID,))
        self.conn.commit()
    def showDatabase(self):
        result = []
        for row in self.c.execute('SELECT * FROM board'):
            result.append(row)
        return result

#def addEntry(entry, database):
#    conn = sqlite3.connect(database)
#    c = conn.cursor()
#    c.execute("CREATE TABLE IF NOT EXISTS board(ID integer PRIMARY KEY UNIQUE, content text)")
#    c.execute("INSERT INTO board(content) Values(?)", (entry,))
#    conn.commit()
#
#def showDatabase(database):
#    result = []
#    conn = sqlite3.connect(database)
#    c = conn.cursor()
#    for row in c.execute('SELECT*FROM board'):
#        result.append(row)
#    return result
