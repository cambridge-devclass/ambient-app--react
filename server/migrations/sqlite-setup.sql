-- Example migration

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  display_name TEXT,
  email TEXT UNIQUE,
  bio TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  created_by INTEGER DEFAULT 0,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_by INTEGER DEFAULT 0,
  is_active BOOLEAN DEFAULT TRUE NOT NULL
);

CREATE UNIQUE INDEX idx_users_username ON users (username);
