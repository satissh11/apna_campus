import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

cols = [col[1] for col in cur.execute("PRAGMA table_info(locations)").fetchall()]
if "lat" not in cols:
    cur.execute("ALTER TABLE locations ADD COLUMN lat REAL")
if "lng" not in cols:
    cur.execute("ALTER TABLE locations ADD COLUMN lng REAL")
if "map_label" not in cols:
    cur.execute("ALTER TABLE locations ADD COLUMN map_label TEXT")
if "category" not in cols:
    cur.execute("ALTER TABLE locations ADD COLUMN category TEXT")

updates = [
    (22.7196, 75.8577, "A1 Block - Room 303", "teacher", 1),
    (22.7198, 75.8580, "A1 Block - Dean Office", "teacher", 2),
    (22.7194, 75.8572, "Admin Block - Scholarship", "building", 3),
    (22.7200, 75.8585, "A1 Block - Cyber Lab", "teacher", 4),
]

cur.executemany(
    "UPDATE locations SET lat=?, lng=?, map_label=?, category=? WHERE id=?",
    updates
)

conn.commit()
conn.close()
print("Map coordinates added successfully!")
