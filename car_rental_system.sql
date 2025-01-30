-- Drop existing tables if they exist
DROP TABLE IF EXISTS car;
DROP TABLE IF EXISTS lease_details;
DROP TABLE IF EXISTS user;

-- Car Table
CREATE TABLE car (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- key-id
  make TEXT NOT NULL DEFAULT '', -- mark
  model TEXT NOT NULL DEFAULT '', -- model
  manufactured_year TEXT NOT NULL DEFAULT '', -- manufactured year
  mileage INTEGER NOT NULL DEFAULT 0, -- mileage
  available INTEGER NOT NULL DEFAULT 1, -- available(0-no, 1-yes)
  min_lease_limit INTEGER NOT NULL DEFAULT 0, -- minimum lease limit(0-no limit, >0 limit for days)
  max_lease_limit INTEGER NOT NULL DEFAULT 0, -- maximum lease limit(0-no limit, >0 limit for days)
  deleted_flag INTEGER NOT NULL DEFAULT 0, -- deleted flag(0-normal, 1-deleted)
  created_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- created time
  updated_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- updated time
  deleted_time DATETIME NOT NULL DEFAULT '1900-01-01 00:00:00', -- deleted time
  daily_rent REAL NOT NULL DEFAULT 0.00, -- daily rent
  extra_fee REAL NOT NULL DEFAULT 0.00 -- extra fee
);

-- Lease Details Table
CREATE TABLE lease_details (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- key-id
  user_id INTEGER NOT NULL DEFAULT 0, -- user id
  car_id INTEGER NOT NULL, -- car id
  lease_start_time DATETIME NOT NULL DEFAULT '1900-01-01 00:00:00', -- start time for leasing
  lease_end_time DATETIME NOT NULL DEFAULT '1900-01-01 00:00:00', -- end time for leasing
  interval_days INTEGER NOT NULL DEFAULT 0, -- interval days
  rent REAL NOT NULL DEFAULT 0.00, -- rent
  deleted_flag INTEGER NOT NULL DEFAULT 0, -- deleted flag(0-normal, 1-deleted)
  created_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- created time
  updated_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- updated time
  deleted_time DATETIME NOT NULL DEFAULT '1900-01-01 00:00:00', -- deleted time
  approved_flag INTEGER NOT NULL DEFAULT 0, -- approved flag(0-pending, 1-approved, 2-not approved)
  refusal_reason TEXT NOT NULL DEFAULT '' -- refusal reason
);

-- User Table
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- key-id
  username TEXT NOT NULL DEFAULT '', -- username
  password TEXT NOT NULL DEFAULT '', -- password after encryption
  role_type INTEGER NOT NULL DEFAULT 0, -- the type of user (0-customer, 1-admin)
  deleted_flag INTEGER NOT NULL, -- delete mark(0-normal, 1-deleted)
  created_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- created time
  deleted_time DATETIME NOT NULL DEFAULT '1900-01-01 00:00:00', -- deleted time
  updated_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP -- updated time
);

-- add a default admin user
INSERT INTO user (username, password, role_type, deleted_flag)
VALUES ('admin', '123456', 1, 0);

-- add some default cars
INSERT INTO car (make, model, manufactured_year, mileage, available, min_lease_limit, max_lease_limit, deleted_flag, created_time, updated_time, deleted_time, daily_rent, extra_fee) VALUES
('XIAOMI', 'SU7', 2025, 0, 1, 10, 30, 0, '2025-01-30 06:21:17', '2025-01-30 06:21:17', '1900-01-01 00:00:00', 100.0, 2000.0),
('BMW', 'X6', 2022, 200001, 1, 60, 180, 0, '2025-01-30 06:22:02', '2025-01-30 06:22:02', '1900-01-01 00:00:00', 50.0, 500.0),
('Tesla', 'Model 3', 2023, 15000, 1, 15, 90, 0, '2025-01-30 07:10:00', '2025-01-30 07:10:00', '1900-01-01 00:00:00', 80.0, 100.0),
('Mercedes-Benz', 'C-Class', 2021, 50000, 1, 30, 120, 0, '2025-01-30 08:00:00', '2025-01-30 08:00:00', '1900-01-01 00:00:00', 70.0, 150.0),
('Audi', 'A4', 2022, 30000, 1, 20, 100, 0, '2025-01-30 09:00:00', '2025-01-30 09:00:00', '1900-01-01 00:00:00', 60.0, 120.0),
('Toyota', 'Camry', 2020, 80000, 1, 10, 60, 0, '2025-01-30 10:00:00', '2025-01-30 10:00:00', '1900-01-01 00:00:00', 40.0, 80.0),
('Honda', 'Civic', 2021, 60000, 1, 15, 75, 0, '2025-01-30 11:00:00', '2025-01-30 11:00:00', '1900-01-01 00:00:00', 35.0, 70.0),
('Ford', 'Mustang', 2023, 5000, 1, 25, 150, 0, '2025-01-30 12:00:00', '2025-01-30 12:00:00', '1900-01-01 00:00:00', 90.0, 200.0),
('Nissan', 'Altima', 2022, 40000, 1, 20, 90, 0, '2025-01-30 13:00:00', '2025-01-30 13:00:00', '1900-01-01 00:00:00', 45.0, 90.0),
('Hyundai', 'Sonata', 2021, 70000, 1, 10, 80, 0, '2025-01-30 14:00:00', '2025-01-30 14:00:00', '1900-01-01 00:00:00', 30.0, 60.0);
