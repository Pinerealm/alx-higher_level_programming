-- Lists all shows from the database, 'hbtn_0e_tvshows_rate', and their total rating.
SELECT title, SUM(rate) AS rating
  FROM tv_shows AS s
  LEFT JOIN tv_show_genres AS sg
    ON s.id = sg.show_id
  LEFT JOIN tv_show_ratings AS sr
    ON s.id = sr.show_id
 GROUP BY title
 ORDER BY SUM(rate) DESC;
