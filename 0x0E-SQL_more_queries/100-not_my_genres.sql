-- list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_show.id 
AND tv_show.title = 'Dexter'
WHERE tv_shows_genres.show_id IS NULL
ORDER BY tv_genres.name ASC;
