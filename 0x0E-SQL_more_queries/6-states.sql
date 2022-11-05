-- Creates a database, 'hbtn_0d_usa', and the tables, 'states'.
-- 'states' has the columns, 'id' and 'name'.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
