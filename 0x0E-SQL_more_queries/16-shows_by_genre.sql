-- Lists all shows, and their genres in the database
SELECT title, name
  FROM tv_shows AS ts
  LEFT JOIN tv_show_genres AS tsg
    ON ts.id = tsg.show_id
  LEFT JOIN tv_genres AS tg
    ON tsg.genre_id = tg.id
 ORDER BY title, name;
