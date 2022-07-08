-- 18. No Comedy tonight!
-- ------------------------
-- Script that lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.
-- display: | title | sorted in ascending order by title.

SELECT title
FROM tv_shows
WHERE title NOT IN (

	SELECT title
	FROM tv_genres AS g
		INNER JOIN tv_show_genres
			ON genre_id = g.id
		RIGHT JOIN tv_shows AS s
			ON show_id = s.id
	WHERE g.name = 'Comedy'
)
ORDER BY title;
