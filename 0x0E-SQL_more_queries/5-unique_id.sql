-- Creates the table, 'unique_id',  with the columns, 'id' and 'name'.
-- The 'id' column must be unique with a default value of 1.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
