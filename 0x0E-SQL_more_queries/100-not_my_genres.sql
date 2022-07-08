-- 17. Not my genre
-- ------------------
-- script that uses the hbtn_0d_tvshows database to list
-- all genres not linked to the show Dexter.
-- display: | name | sorted in ascending order by name.

SELECT name
FROM tv_genres
WHERE name NOT IN (

	SELECT name
	FROM tv_shows AS s
		INNER JOIN tv_show_genres
			ON show_id = s.id
		INNER JOIN tv_genres AS g
			ON genre_id = g.id
	WHERE title = 'Dexter'
)
ORDER BY name;
