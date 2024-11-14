import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('personal_finance_tracker.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Create the finances table
cursor.execute('''
CREATE TABLE IF NOT EXISTS finances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    type TEXT NOT NULL,               -- e.g., 'income' or 'expense'
    name TEXT NOT NULL,               -- transaction name
    tag TEXT,                         -- category/tag for transaction
    value REAL NOT NULL,              -- amount of transaction
    date TEXT NOT NULL,               -- date of transaction in 'YYYY-MM-DD' format
    notes TEXT,                       -- optional notes on transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

# Print sucess message
print("Database and tables created successfully.")