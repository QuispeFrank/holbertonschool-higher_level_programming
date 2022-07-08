-- 15. Only Comedy
-- -----------------
-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- display: | title | sorted in ascending order by the show title.

SELECT title
FROM tv_show_genres
	INNER JOIN tv_genres AS g
		ON g.id = genre_id
	INNER JOIN tv_shows AS s
		ON s.id = show_id
WHERE name = 'Comedy'
ORDER BY title;
