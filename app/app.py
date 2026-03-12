import time
import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Wait for MySQL to be ready
db = None
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpass",
            database="partsdb"
        )
        break
    except mysql.connector.Error:
        print("MySQL not ready, retrying in 5 seconds...")
        time.sleep(5)

if db is None:
    raise Exception("Could not connect to MySQL after 10 attempts")

cursor = db.cursor()

# Home page


@app.route("/")
def home():
    category = request.args.get("category")
    search = request.args.get("search")

    cursor.execute("SELECT DISTINCT category FROM parts ORDER BY category ASC")
    categories = [row[0] for row in cursor.fetchall()]

    if category and search:
        cursor.execute(
            "SELECT id, category, model, specs FROM parts WHERE category=%s AND (model LIKE %s OR specs LIKE %s)",
            (category, f"%{search}%", f"%{search}%")
        )
    elif category:
        cursor.execute(
            "SELECT id, category, model, specs FROM parts WHERE category=%s", (category,))
    elif search:
        cursor.execute(
            "SELECT id, category, model, specs FROM parts WHERE model LIKE %s OR specs LIKE %s OR category LIKE %s",
            (f"%{search}%", f"%{search}%", f"%{search}%")
        )
    else:
        cursor.execute("SELECT id, category, model, specs FROM parts")

    parts = cursor.fetchall()
    return render_template("index.html", parts=parts, categories=categories)

# Add New Part page


@app.route("/add", methods=["GET", "POST"])
def add_part():

    cursor.execute("SELECT DISTINCT category FROM parts")
    categories = [row[0] for row in cursor.fetchall()]

    if request.method == "POST":
        category = request.form["category"].strip().upper()
        model = request.form["model"]
        specs = request.form["specs"]
        cursor.execute(
            "INSERT INTO parts (category, model, specs) VALUES (%s, %s, %s)",
            (category, model, specs)
        )
        db.commit()
        return redirect("/")
    return render_template("add_part.html", categories=categories)

# Edit Part page


@app.route("/edit/<int:part_id>", methods=["GET", "POST"])
def edit_part(part_id):
    if request.method == "POST":
        category = request.form["category"].strip().upper()
        model = request.form["model"]
        specs = request.form["specs"]
        cursor.execute(
            "UPDATE parts SET category=%s, model=%s, specs=%s WHERE id=%s",
            (category, model, specs, part_id)
        )
        db.commit()
        return redirect("/")

    cursor.execute("SELECT DISTINCT category FROM parts")
    categories = [row[0] for row in cursor.fetchall()]

    cursor.execute(
        "SELECT id, category, model, specs FROM parts WHERE id=%s", (part_id,))
    part = cursor.fetchone()
    return render_template("edit_part.html", part=part, part_id=part_id, categories=categories)

# Delete Part page


@app.route("/delete/<int:part_id>", methods=["POST"])
def delete_part(part_id):
    cursor.execute("DELETE FROM parts WHERE id=%s", (part_id,))
    db.commit()
    return redirect("/")


app.run(host="0.0.0.0", port=5000)
