-- 14. My genres
-- ---------------
-- Script that uses the hbtn_0d_tvshows database to lists all
-- genres of the show Dexter.
-- display: | name | sorted in ascending order by the genre name.

SELECT name
FROM tv_show_genres
	INNER JOIN tv_genres AS g
		ON g.id = genre_id 
	INNER JOIN tv_shows AS s
		ON s.id = show_id
WHERE title = 'Dexter'
ORDER BY name;
