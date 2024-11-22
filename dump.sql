PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO users VALUES(1,'Quintian','scrypt:32768:8:1$VtZDSQGJD7I7yQ0S$ee0cd7002ba9a4bf1e37d891a110fb18b7d66e064e9c7b568b8867f612373d2b4bc4cc3cec37f641437a23775832368a07e41e344dc25c1c950dc487696176a6','2024-11-13 22:54:01','2024-11-13 22:54:01');
CREATE TABLE finances (
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
);
INSERT INTO sqlite_sequence VALUES('users',1);
INSERT INTO sqlite_sequence VALUES('finances',3);
COMMIT;
