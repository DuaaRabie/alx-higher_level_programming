-- Lists all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE NOT EXISTS (
	SELECT *
	FROM tv_show_genres
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_show_genres.genre_id = tv_genres.id AND tv_shows.title = 'Dexter'
)
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
