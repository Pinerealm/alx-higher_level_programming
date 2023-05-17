-- List all records from second_table with a score >= 10.
SELECT score, name
  FROM second_table
 WHERE score >= 10
 ORDER BY score DESC;
