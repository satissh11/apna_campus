from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Search function
def search_data(search_text):
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    query = """
    SELECT * FROM locations
    WHERE name LIKE ? OR type LIKE ? OR block LIKE ? OR floor LIKE ? OR room LIKE ?
    """
    param = ('%' + search_text + '%',)*5
    cur.execute(query, param)
    data = cur.fetchall()
    conn.close()
    return data
@app.route('/')
def landing():
    return render_template("landing.html")  # Landing page dikhega pehle

@app.route('/searchpage')
def searchpage():
    return render_template("index.html")   # Search page route


@app.route('/search', methods=['POST'])
def search():
    search_text = request.form['search']
    result = search_data(search_text)
    return render_template("result.html", result=result, search_text=search_text)

if __name__ == "__main__":
    app.run(debug=True)
