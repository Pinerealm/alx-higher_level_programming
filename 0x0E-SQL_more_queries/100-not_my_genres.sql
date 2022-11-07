-- List all genres not linked with the show 'Dexter'
SELECT *
  FROM tv_genres AS g
 WHERE name NOT IN (SELECT name
                      FROM tv_genres AS g
                     INNER JOIN tv_show_genres AS sg
                        ON g.id = sg.genre_id
                     INNER JOIN tv_shows AS s
                        ON sg.show_id = s.id
                     WHERE s.title = 'Dexter')
 ORDER BY name;
