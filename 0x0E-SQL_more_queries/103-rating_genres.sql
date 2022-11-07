-- List all genres and the sum of ratings for each
SELECT name, SUM(rate) AS rating
  FROM tv_genres AS g
 INNER JOIN tv_show_genres AS sg
    ON g.id = sg.genre_id
 INNER JOIN tv_show_ratings AS sr
    ON sg.show_id = sr.show_id
 GROUP BY name
 ORDER BY SUM(rate) DESC;
