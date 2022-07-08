-- 20. Best genre
-- ----------------
-- script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating.
-- display: | name - rating | sorted in descending order by rating.

SELECT g.name, SUM(rate) AS 'rating'
FROM tv_show_ratings AS tsr
	INNER JOIN tv_show_genres AS tsg
		ON tsg.show_id = tsr.show_id	
	INNER JOIN tv_genres AS g
		ON tsg.genre_id = g.id
GROUP BY g.name
ORDER BY rating DESC;
