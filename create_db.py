import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    block TEXT,
    floor TEXT,
    room TEXT
)
""")

# optional: data insert (sirf ek baar)
cur.execute("""
INSERT OR IGNORE INTO locations VALUES
(1,'CSE Department','Department','A','2','201'),
(2,'ECE Department','Department','B','1','105'),
(3,'Dr. Sharma','Teacher','A1','3','304'),
""")

conn.commit()
conn.close()

print("Database & table READY")
