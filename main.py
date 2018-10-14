import gkeepapi
import sqlite3
import gdbm

# keep = gkeepapi.Keep()
# succes = keep.login('tomkobat@gmail.com', 'amirkuspapirkus')
# note = keep.findLabel("poznamky")

# finaltext = ""

# gnotes = keep.all()
# for note in gnotes:
#     finaltext += note.text

# # with open("ahoj.txt", "a") as ahoj:
# #     ahoj.write(finaltext)

# finaltext = [s.strip() for s in finaltext.splitlines()]

# list_links = list()
# count = 0
# for text in finaltext:
#     if text.startswith("http"):
#         list_links.append(text)
#         count += 1

# print(list_links)

db = sqlite3.connect('/home/tomas/.mozilla/firefox/4mjkjidl.default/places.sqlite')
"""INSERT INTO moz_bookmarks(type, fk, parent, position)"""



# gnote = keep.createNote('cauuuu', 'jakjeeeeeeee')

# glist = keep.createList('Title', [
#     ('Item 2', True)  # Checked
# ])


# keep.sync()