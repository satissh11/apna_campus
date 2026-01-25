from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# database se data laane ka function
def get_location(search_text):
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM locations WHERE name LIKE ?",
        ('%' + search_text + '%',)
    )
    data = cur.fetchall()
    conn.close()
    return data

# home page
@app.route('/')
def home():
    return render_template("index.html")

# search page
@app.route('/search', methods=['POST'])
def search():
    text = request.form['search']
    result = get_location(text)
    return render_template("result.html", result=result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

