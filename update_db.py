import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

updates = [
    ('Dr. Priyanka Srivastav', 'Program Coordinator', 'A1', '3', '303', 1),
    ('Dr. Pankaj Goswami', 'Dean of College', 'A1', 'G', '101', 2),
    ('Scholarship', 'E-kalyan', 'Admin', '3', '309', 3),
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

