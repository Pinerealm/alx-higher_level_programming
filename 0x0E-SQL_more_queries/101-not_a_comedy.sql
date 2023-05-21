-- Lists all shows that are not comedy
SELECT title
  FROM tv_shows AS ts
 WHERE ts.id NOT IN (SELECT show_id
                      FROM tv_show_genres AS tsg
                     INNER JOIN tv_genres AS tg
                        ON tsg.genre_id = tg.id
                     WHERE tg.name = 'Comedy')
 ORDER BY title;
