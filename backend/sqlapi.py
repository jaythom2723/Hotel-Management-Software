import sqlite3 as sql

from ctypes import LogbookEntryMessage

_connection = None
_cursor = None

def initializeSQL():
    try:
        global _connection, _cursor
        _connection = sql.connect('db.db')
        _cursor = _connection.cursor()

        _initTables()
    except sql.Error as error:
        print("Error occurred - ", error)

def _initTables():
    try:
        global _cursor
        _cursor.execute('create table if not exists LOGBOOK (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, code TEXT, total REAL);')
    except sql.Error as error:
        print("Error occurred - ", error)

def closeSQL():
    try:
        global _connection, _cursor
        _cursor.close()
        _connection.close()
    except sql.Error as error:
        print("Error occurred - ", error)




# The following functions are used in various other frontend files in order to send data to the database
def sendLogbookEntry(entry: LogbookEntryMessage):
    try:
        global _cursor, _connection
       
        _cursor.execute(f'insert into LOGBOOK (date, code, total) values ("{entry.date}", "{entry.code}", {entry.total})')
        _connection.commit()
    except sql.Error as error:
        print("Error occurred - ", error)

def getLogbookEntriesByDate(date) -> list[LogbookEntryMessage]:
    try:
        global _cursor, _connection
        ret = []
        
        _cursor.execute(f'select * from LOGBOOK where date = "{date}"')
        items = _cursor.fetchall()
        for item in items:
            message = LogbookEntryMessage(item[1], item[2], item[3])
            ret.append(message)
        return ret
    except sql.Error as error:
        print("Error occurred - ", error)
        return []
