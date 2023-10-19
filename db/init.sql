CREATE DATABASE sample_db;
USE sample_db;

CREATE TABLE IF NOT EXISTS datetime_table (
    temp_entry_id varchar(500) PRIMARY KEY UNIQUE, 
    datetime_id TEXT
);

INSERT INTO datetime_table VALUES ('sdaac123', 'test_insert_on_build');
