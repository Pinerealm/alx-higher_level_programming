-- Lists all genres of the show, Dexter
SELECT name
  FROM tv_genres AS g
 INNER JOIN tv_show_genres AS sg
    ON g.id = sg.genre_id
 INNER JOIN tv_shows AS s
    ON sg.show_id = s.id
 WHERE s.title = 'Dexter'
 ORDER BY name;
