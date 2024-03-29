--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE NOT EXISTS (
        SELECT *
        FROM tv_show_genres
        JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
        WHERE tv_show_genres.show_id = tv_shows.id AND tv_genres.name = 'Comedy'
)
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;
