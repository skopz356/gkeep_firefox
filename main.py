import gkeepapi
import sqlite3
import os


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



class SyncLinks():
    def __init__(self, **kwargs):
        if "path" in kwargs:
            self.path = kwargs["path"]

    def path_mozzilla(self):
        if os.path.isdir(os.path.join("/home/tomas", ".mozilla")):
            return [x for x in list(os.listdir(os.path.join("/home/tomas", ".mozilla/firefox"))) if x.endswith(".default")][0]
        elif os.path.isdir(self.path):
            return [x for x in os.listdir(self.path) if x.endswith(".default")][0]
        else:
            raise FileNotFoundError(
                "Folder of mozila could not be"
            )

    def get_places_sql(self):
        return os.path.join(self.path_mozzilla(), "places.sql")
            
        
        
s = SyncLinks()
print(s.get_places_sql())


        

            
        