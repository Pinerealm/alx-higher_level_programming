-- Lists all genres of the show, Dexter
SELECT name
  FROM tv_genres AS tg
 INNER JOIN tv_show_genres AS tsg
    ON tg.id = tsg.genre_id
 WHERE tsg.show_id = (SELECT id
                        FROM tv_shows
                       WHERE title = 'Dexter')
 ORDER BY name;
