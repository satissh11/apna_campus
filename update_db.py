import sqlite3

# Database connect
conn = sqlite3.connect("campus.db")
cur = conn.cursor()

# ----------------------------
# Step 1: Check & add missing columns
# ----------------------------
existing_columns = [col[1] for col in cur.execute("PRAGMA table_info(locations)").fetchall()]

# Required columns
required_columns = {
    'role': 'TEXT',
    'sitting_block': 'TEXT',
    'floor': 'TEXT',
    'room_no': 'TEXT'
}

for col, col_type in required_columns.items():
    if col not in existing_columns:
        cur.execute(f"ALTER TABLE locations ADD COLUMN {col} {col_type}")
        print(f"Added missing column '{col}'")

# ----------------------------
# Step 2: Prepare data to update
# ----------------------------
updates = [
    ('Dr. Priyanka Srivastav', 'Program Coordinator', 'A1', '3', '303', 1),
    ('Dr. Pankaj Goswami', 'Dean of College', 'A1', 'G', '101', 2),
    ('Scholarship', 'E-kalyan', 'Admin', '3', '309', 3),
    ('Mr. Bikram Pratap Singh', 'Cyber Expert', 'A1', '5', '504', 4),
]

# ----------------------------
# Step 3: Update multiple columns in one query
# ----------------------------
cur.executemany("""
UPDATE locations
SET
    name = ?,
    role = ?,
    sitting_block = ?,
    floor = ?,
    room_no = ?
WHERE id = ?
""", updates)

# ----------------------------
# Step 4: Save changes and close
# ----------------------------
conn.commit()
conn.close()

print("Database updated successfully!")
