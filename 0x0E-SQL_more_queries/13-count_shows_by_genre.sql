-- Display no of shows per genre in 'hbtn_0d_tvshows'
SELECT name AS genre, COUNT(show_id) AS number_of_shows
  FROM tv_genres AS tg
 INNER JOIN tv_show_genres AS tsg
    ON tg.id = tsg.genre_id
 GROUP BY name
 ORDER BY number_of_shows DESC;
