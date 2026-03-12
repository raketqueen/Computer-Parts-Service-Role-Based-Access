import sqlite3

# connect to database (file will be created automatically)
conn = sqlite3.connect("pc_parts.db")
cursor = conn.cursor()

# create the parts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    brand TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully")
