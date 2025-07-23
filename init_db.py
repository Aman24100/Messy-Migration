# import sqlite3

# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     password TEXT NOT NULL
# )
# ''')

# cursor.execute("INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password123')")
# cursor.execute("INSERT INTO users (name, email, password) VALUES ('Jane Smith', 'jane@example.com', 'secret456')")
# cursor.execute("INSERT INTO users (name, email, password) VALUES ('Bob Johnson', 'bob@example.com', 'qwerty789')")

# conn.commit()
# conn.close()

# print("Database initialized with sample data")



# init_db.py
import os
import sqlite3

DB_PATH = os.getenv("DATABASE_PATH", "users.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# seed sample users
users = [
    ('John Doe',    'john@example.com',   'password123'),
    ('Jane Smith',  'jane@example.com',   'secret456'),
    ('Bob Johnson', 'bob@example.com',    'qwerty789'),
]
cursor.executemany(
    "INSERT INTO users (name, email, password) VALUES (?,?,?)",
    users
)

conn.commit()
conn.close()
print(f"Database initialized at {DB_PATH} with sample data")
