CREATE DATABASE sample_db;
USE sample_db;

CREATE TABLE IF NOT EXISTS sample_table (
    temp_entry_id varchar(500) PRIMARY KEY UNIQUE, 
    datetime_id TEXT
);