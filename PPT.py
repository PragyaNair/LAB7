import sqlite3
from faker import Faker
from datetime import datetime

# Create a fake data generator
fake = Faker()

# Connect to the database (creates a new database if it doesn't exist)
con = sqlite3.connect('people.db')
cursor = con.cursor()

# Create the people table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        created_at TEXT,
        updated_at TEXT
    )
''')

# Generate and insert fake data into the people table
for _ in range(200):
    name = fake.name()
    age = fake.random_int(min=1, max=100)
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = created_at
    cursor.execute('''
        INSERT INTO people (name, age, created_at, updated_at)
        VALUES (?, ?, ?, ?)
    ''', (name, age, created_at, updated_at))

# Commit the changes and close the connection
con.commit()
con.close()
