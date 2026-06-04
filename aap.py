from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def search_data(search_text):
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    query = """
    SELECT id, name, type, block, floor, room, role, sitting_block, room_no,
           lat, lng, map_label, category, description, directions, building_icon
    FROM locations
    WHERE name LIKE ? OR type LIKE ? OR block LIKE ? OR floor LIKE ?
       OR room LIKE ? OR role LIKE ? OR category LIKE ? OR description LIKE ?
    """
    p = '%' + search_text + '%'
    cur.execute(query, (p, p, p, p, p, p, p, p))
    data = cur.fetchall()
    conn.close()
    return data

def get_all_locations():
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT name, category, building_icon, role, block, floor, room, description
        FROM locations ORDER BY category, name
    """)
    data = cur.fetchall()
    conn.close()
    return data

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/searchpage')
def searchpage():
    all_locations = get_all_locations()
    return render_template("index.html", all_locations=all_locations)

@app.route('/search', methods=['POST'])
def search():
    search_text = request.form['search']
    result = search_data(search_text)
    return render_template("result.html", result=result, search_text=search_text)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)