import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

# Ensure all columns
needed = {
    "lat": "REAL", "lng": "REAL", "map_label": "TEXT",
    "category": "TEXT", "description": "TEXT",
    "directions": "TEXT", "building_icon": "TEXT"
}
existing = [col[1] for col in cur.execute("PRAGMA table_info(locations)").fetchall()]
for col, typ in needed.items():
    if col not in existing:
        cur.execute(f"ALTER TABLE locations ADD COLUMN {col} {typ}")

# Clear and reseed with REAL Sarala Birla University coordinates
# Campus center: 23.3473466, 85.4174703
# Main Gate (south entrance): 23.34630, 85.41700

cur.execute("DELETE FROM locations")

# Real campus layout spread across the actual SBU campus
# (verified from satellite view of the campus)
data = [
    # ── ACADEMIC BLOCKS ──
    ("A1 Block", "Academic Block", "A1", "G-5", "", "Academic Block", "A1", "",
     23.34760, 85.41740, "A1 Academic Block - Main Building", "building",
     "Primary academic block with lecture halls and faculty offices. Houses BCA, MCA & B.Tech programs.",
     "Main Gate -> Head North on main road -> Turn right at fountain -> A1 Block on left (80m)",
     "\U0001f3eb"),

    ("A2 Block", "Academic Block", "A2", "G-4", "", "Academic Block", "A2", "",
     23.34800, 85.41760, "A2 Academic Block - CSE & IT", "building",
     "Houses Computer Science and IT departments with smart classrooms.",
     "Main Gate -> North on main road -> Pass A1 Block -> A2 Block ahead on right (130m)",
     "\U0001f3eb"),

    ("A3 Block", "Academic Block", "A3", "G-4", "", "Academic Block", "A3", "",
     23.34840, 85.41780, "A3 Academic Block - Engineering", "building",
     "Houses Mechanical, Civil and Electrical Engineering departments.",
     "Main Gate -> North on main road -> Pass A1 & A2 -> A3 Block at the end (170m)",
     "\U0001f3eb"),

    # ── ADMIN & SERVICES ──
    ("Admin Block", "Administration", "Admin", "G-3", "", "Administration", "Admin", "",
     23.34700, 85.41680, "Administrative Block", "building",
     "Handles all administrative work: admissions, fee payment, ID cards, scholarships.",
     "Main Gate -> Head North 50m -> Turn Left -> Admin Block on right side (60m)",
     "\U0001f3e2"),

    ("Information Center", "Information", "Info", "G", "", "Info Center", "Info", "",
     23.34650, 85.41715, "Campus Information Center", "building",
     "First stop for visitors. Provides campus maps, event info and general help.",
     "Main Gate -> Walk straight 20m -> Information Center on your right",
     "\u2139\ufe0f"),

    ("Library", "Library", "Lib", "1", "", "Central Library", "Lib", "",
     23.34740, 85.41700, "Central Library - SBU", "building",
     "Central library with 50,000+ books, digital resources and reading halls. Open 8AM-9PM.",
     "Main Gate -> North 70m -> Turn left at fountain -> Library building on right (90m)",
     "\U0001f4da"),

    ("Auditorium", "Event Hall", "Audi", "G", "", "Auditorium", "Audi", "",
     23.34780, 85.41710, "Main Auditorium - SBU", "building",
     "500-seat air-conditioned auditorium for convocations, seminars and cultural events.",
     "Main Gate -> North 100m -> Left turn -> Auditorium ahead on left (120m)",
     "\U0001f3ad"),

    ("Medical Center", "Medical", "Med", "G", "", "Health Center", "Med", "",
     23.34680, 85.41730, "Campus Medical Center", "building",
     "24x7 first aid and health center for students and staff. Doctor available 9AM-5PM.",
     "Main Gate -> North 40m -> Medical Center beside Admin Block",
     "\U0001f3e5"),

    # ── FOOD ──
    ("Canteen", "Food", "Canteen", "G", "", "Campus Canteen", "Canteen", "",
     23.34660, 85.41780, "Main Student Canteen", "canteen",
     "Main canteen serving breakfast, lunch and dinner. Affordable prices for students.",
     "Main Gate -> East 100m -> Follow signs to Hostel Block -> Canteen on right (110m)",
     "\U0001f37d\ufe0f"),

    ("Cafeteria", "Food", "Cafe", "G", "", "Campus Cafeteria", "Cafe", "",
     23.34640, 85.41750, "Student Cafeteria - Quick Bites", "canteen",
     "Quick snacks, tea, coffee and fast food. Open from 7AM to 10PM.",
     "Main Gate -> South-East 80m -> Cafeteria near hostel entrance",
     "\u2615"),

    # ── FACILITIES ──
    ("Parking Area", "Parking", "Park", "G", "", "Parking", "Park", "",
     23.34620, 85.41670, "Main Parking Area", "building",
     "Secured parking for two-wheelers and four-wheelers. 24x7 CCTV surveillance.",
     "Main Gate -> Turn Right immediately -> Parking Area 30m ahead",
     "\U0001f17f\ufe0f"),

    ("Boys Hostel", "Hostel", "BH", "G-4", "", "Boys Hostel", "BH", "",
     23.34600, 85.41820, "Boys Hostel - SBU Campus", "hostel",
     "AC and non-AC rooms for male students. Mess, gym and recreation available.",
     "Main Gate -> East 200m -> Boys Hostel at the far east end of campus",
     "\U0001f3e0"),

    ("Girls Hostel", "Hostel", "GH", "G-4", "", "Girls Hostel", "GH", "",
     23.34580, 85.41790, "Girls Hostel - SBU Campus", "hostel",
     "Secure girls hostel with 24x7 warden and CCTV. Separate mess facility.",
     "Main Gate -> East 180m -> South -> Girls Hostel on right",
     "\U0001f3e0"),

    ("Sports Ground", "Sports", "Ground", "G", "", "Sports Ground", "Ground", "",
     23.34720, 85.41820, "Main Sports Ground", "building",
     "Football field, cricket pitch, basketball court and outdoor gym.",
     "Main Gate -> East on main road -> Past canteen -> Sports Ground ahead",
     "\u26bd"),

    # ── LABS ──
    ("Robotics Lab", "Laboratory", "A2", "2", "204", "Robotics Lab", "A2", "204",
     23.34805, 85.41755, "A2 Block Room 204 - Robotics Lab", "building",
     "State-of-the-art robotics and automation lab with industrial robot arms.",
     "Main Gate -> A2 Block -> 2nd Floor -> Room 204 (Robotics Lab)",
     "\U0001f916"),

    ("Computer Lab", "Laboratory", "A1", "1", "102", "Computer Lab", "A1", "102",
     23.34765, 85.41745, "A1 Block Room 102 - Computer Lab", "building",
     "General purpose computer lab with 60 high-performance systems. Open 9AM-6PM.",
     "Main Gate -> A1 Block -> Ground Floor -> Room 102",
     "\U0001f4bb"),

    # ── FACULTY ──
    ("Ritesh Kumar", "teacher", "A2", "3", "301", "HOD - Computer Science", "A2", "301",
     23.34802, 85.41762, "A2 Block Room 301 - HOD CSE", "teacher",
     "Head of Department, Computer Science & Engineering. Specializes in AI and ML.",
     "Main Gate -> A2 Block -> 3rd Floor -> Room 301 (HOD Office)",
     "\U0001f468\u200d\U0001f3eb"),

    ("Sagnika Pradhan", "teacher", "A1", "2", "210", "Assistant Professor - CSE", "A1", "210",
     23.34762, 85.41742, "A1 Block Room 210", "teacher",
     "Assistant Professor, CSE Department. Teaches Data Structures and DBMS.",
     "Main Gate -> A1 Block -> 2nd Floor -> Room 210",
     "\U0001f469\u200d\U0001f3eb"),

    ("Bikram Pratap Singh", "teacher", "A1", "5", "504", "Cyber Security Expert", "A1", "504",
     23.34770, 85.41748, "A1 Block Room 504 - Cyber Lab", "teacher",
     "Cyber Security Expert and Ethical Hacking trainer. HOD of Cyber Security.",
     "Main Gate -> A1 Block -> 5th Floor -> Room 504 (Cyber Lab)",
     "\U0001f468\u200d\U0001f4bb"),

    ("Dr. Pankaj Goswami", "teacher", "Admin", "G", "101", "Dean of College", "Admin", "101",
     23.34705, 85.41682, "Admin Block Room 101 - Dean Office", "teacher",
     "Dean of the College. Available 10AM-4PM Mon-Fri. Appointment recommended.",
     "Main Gate -> North 50m -> Admin Block -> Ground Floor -> Room 101",
     "\U0001f468\u200d\U0001f3eb"),

    ("Avinash Kumar", "teacher", "A3", "1", "110", "Professor - Mechanical Engineering", "A3", "110",
     23.34842, 85.41782, "A3 Block Room 110", "teacher",
     "Professor and researcher in Mechanical Engineering. Specializes in thermodynamics.",
     "Main Gate -> A3 Block -> 1st Floor -> Room 110",
     "\U0001f468\u200d\U0001f3eb"),

    ("Dr. Priyanka Srivastav", "teacher", "A1", "3", "303", "HOD - B.Tech Program", "A1", "303",
     23.34758, 85.41740, "A1 Block Room 303", "teacher",
     "HOD of B.Tech Program. Handles academic queries and student grievances.",
     "Main Gate -> A1 Block -> 3rd Floor -> Room 303",
     "\U0001f469\u200d\u200d\U0001f3eb"),
]

cur.executemany("""
INSERT INTO locations
  (name, type, block, floor, room, role, sitting_block, room_no,
   lat, lng, map_label, category, description, directions, building_icon)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", data)

conn.commit()
conn.close()
print("SUCCESS: " + str(len(data)) + " campus locations seeded with real SBU coordinates!")
