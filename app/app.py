from flask import session, flash
import time
import mysql.connector
from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

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

app.secret_key = "your_secret_key_here"  # Add this for session management

# Helper function to require login


def login_required(f):
    from functools import wraps

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to access this page")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Login page


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    cursor.execute(
        "SELECT id, username, password, role FROM users WHERE username=%s",
        (username,)
    )

    user = cursor.fetchone()

    if user and check_password_hash(user[2], password):
        session["user_id"] = user[0]
        session["username"] = user[1]
        session["role"] = user[3]
        flash("Login successful")
    else:
        flash("Invalid username or password")

    return redirect("/")


# Logout page
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    flash("You have been logged out successfully")
    return redirect("/")


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


@login_required
@app.route("/add", methods=["GET", "POST"])
def add_part():
    if session.get("role") != "admin":
        flash("You do not have permission to access this page")
        return redirect("/")

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


@login_required
@app.route("/edit/<int:part_id>", methods=["GET", "POST"])
def edit_part(part_id):
    if session.get("role") not in ["admin", "editor"]:
        flash("You do not have permission to edit this part")
        return redirect("/")

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


@login_required
@app.route("/delete/<int:part_id>", methods=["POST"])
def delete_part(part_id):
    if session.get("role") != "admin":
        flash("You do not have permission to delete this part")
        return redirect("/")

    cursor.execute("DELETE FROM parts WHERE id=%s", (part_id,))
    db.commit()
    return redirect("/")


app.run(host="0.0.0.0", port=5000)
