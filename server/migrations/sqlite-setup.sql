-- Example migration

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE not null,
  password_hash TEXT not null,
  display_name TEXT,
  email TEXT UNIQUE,
  bio TEXT,
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  created_by INTEGER DEFAULT 0,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP,
  updated_by INTEGER DEFAULT 0,
  is_active BOOLEAN DEFAULT TRUE
);
