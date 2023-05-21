-- List all shows in the database, 'hbtn_0d_tvshows',
-- Display the title of the show, and the genre_id linked to it.
SELECT ts.title, tsg.genre_id
  FROM tv_shows AS ts
  LEFT JOIN tv_show_genres AS tsg
    ON ts.id = tsg.show_id
 ORDER BY ts.title, tsg.genre_id;
