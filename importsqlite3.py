import sqlite3
# You must create a database. Please run this file in your editor.
# Please install requirements as explained on there website https://bottlepy.org/docs/dev/index.html.
conn = sqlite3.connect('simple-database.db')
conn.execute(
    "CREATE TABLE item (id INTEGER PRIMARY KEY, title char(100) NOT NULL, content char(100) NOT NULL)")
conn.execute(
    "INSERT INTO item (title,content) VALUES ('The cat','says miaow')")
conn.execute(
    "INSERT INTO item (title,content) VALUES ('The dog','woff')")
conn.execute(
    "INSERT INTO item (title,content) VALUES ('The hamster','says niff')")
conn.execute(
    "INSERT INTO item (title,content) VALUES ('The Pig','says oink')")
conn.commit()
