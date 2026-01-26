import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

updates = [
    ('Dr. priyanka srivastav', 'coordinator of mca', 'A1', '3', '303', 1),
    ('dr. pankaj goswami', 'Dean', 'A1', 'G', '100', 2),
    ('scholarship', 'e-kalyan', 'Admin', '3', '309', 3),
    ('Mr. Bikram Pratap Singh', 'Cyber Expert', 'A1', '5', '504', 4),
]

cur.executemany("""
UPDATE locations
SET
    name = ?,
    type = ?,
    block = ?,
    floor = ?,
    room = ?
WHERE id = ?
""", updates)

conn.commit()
conn.close()

print("Database updated successfully")


# git add campus.db
# git commit -m "Update database for live website"
# git push

