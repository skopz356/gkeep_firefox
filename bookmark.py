import sqlite3

class Bookmark():
    FIREFOX_SQL = "/home/tomas/.mozilla/firefox/4mjkjidl.default/places.sqlite"
    db = sqlite3.connect(FIREFOX_SQL)
    cursor =db.cursor()
    cursor.execute('''INSERT INTO moz_bookmarks()''')
    # def crbookmark(links):
        

