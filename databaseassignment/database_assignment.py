import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('files.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS txt_files (
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        filename TEXT
    )''')

for file in fileList:
    if file.endswith('.txt'):
        cur.execute('''
        INSERT INTO txt_files (filename)
        VALUES (?)
        ''', (file,))
        print(f"Added to database: {file}")

conn.commit()

cur.execute('SELECT * FROM txt_files')
rows = cur.fetchall()

print("\nText files in the database:")
for row in rows:
    print(f"ID: {row[0]}, Filename: {row[1]}")

conn.close()
