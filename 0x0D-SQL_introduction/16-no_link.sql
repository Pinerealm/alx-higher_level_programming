-- Display rows with non-null names in second_table.
-- Only display the name and score columns.
SELECT score, name
  FROM second_table
 WHERE name IS NOT NULL
 ORDER BY score DESC;
