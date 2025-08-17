-- Example migration

CREATE TABLE person (
  id INT UNIQUE AUTO_INCREMENT,
  login_name varchar(20) UNIQUE not null,
  fullname varchar(100) not null,
	email varchar(100) UNIQUE not null,
  bio varchar(200),
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  created_by int DEFAULT 0,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP,
  updated_by int DEFAULT 0,
  is_active BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (id)
);