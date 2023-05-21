-- List all genres not linked with the show 'Dexter'
SELECT name
  FROM tv_genres
 WHERE name NOT IN (SELECT name
                      FROM tv_genres AS tg
                     INNER JOIN tv_show_genres AS tsg
                        ON tg.id = tsg.genre_id
                     INNER JOIN tv_shows AS ts
                        ON tsg.show_id = ts.id
                     WHERE ts.title = 'Dexter')
 ORDER BY name;