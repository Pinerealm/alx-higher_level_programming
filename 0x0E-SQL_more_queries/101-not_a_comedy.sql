-- Lists all shows that are not comedy
SELECT title
  FROM tv_shows AS s
 WHERE s.id NOT IN (SELECT show_id
                      FROM tv_show_genres AS sg
                     INNER JOIN tv_genres AS g
                        ON sg.genre_id = g.id
                     WHERE g.name = 'Comedy')
 ORDER BY s.title;
