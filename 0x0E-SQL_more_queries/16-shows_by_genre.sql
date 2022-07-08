-- 16. List shows and genres
-- ---------------------------
-- Script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
-- display: | title - name | sorted in ascending order
-- 	    by the title and name.

SELECT title, name
FROM tv_show_genres
	INNER JOIN tv_genres AS g
		ON g.id = genre_id
	RIGHT JOIN tv_shows AS s
		ON s.id = show_id
ORDER BY title, name;
