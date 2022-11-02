-- List the number of records for each score in second_table.
SELECT score, COUNT(*)
  FROM second_table
 GROUP BY score
 ORDER BY score DESC;
