-- GIO Electronics — MySQL-ready schema
-- Not connected by default; the site currently runs on the in-memory data in
-- data.py and a local JSON file for enquiries (database/enquiries.json).
-- This schema is ready to use once a MySQL server is configured (see
-- config.py for connection settings).

CREATE DATABASE IF NOT EXISTS gio_electronics
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE gio_electronics;

CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  slug VARCHAR(150) NOT NULL UNIQUE,
  category VARCHAR(100) NOT NULL,
  description TEXT,
  overview TEXT,
  image VARCHAR(255),
  specifications JSON,
  material VARCHAR(255),
  dimensions VARCHAR(255),
  compatibility VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(150) NOT NULL,
  company_name VARCHAR(150) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  phone VARCHAR(30),
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS enquiries (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT NULL,
  name VARCHAR(150) NOT NULL,
  company_name VARCHAR(150) NOT NULL,
  email VARCHAR(150) NOT NULL,
  phone VARCHAR(30) NOT NULL,
  product_service VARCHAR(150),
  quantity VARCHAR(50),
  message TEXT NOT NULL,
  attachment VARCHAR(255),
  status ENUM('new', 'in_review', 'quoted', 'closed') NOT NULL DEFAULT 'new',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_enquiries_customer FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL
) ENGINE=InnoDB;
