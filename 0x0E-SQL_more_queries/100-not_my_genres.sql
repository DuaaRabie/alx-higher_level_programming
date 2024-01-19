-- list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_show.id 
WHERE tv_show.title != 'Dexter' and tv_shows_genres.name IS NULL
ORDER BY tv_genres.name ASC;
