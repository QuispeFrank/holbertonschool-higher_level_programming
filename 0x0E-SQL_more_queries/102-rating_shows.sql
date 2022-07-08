-- 19. Rotten tomatoes
-- ---------------------
-- Script that lists all shows from hbtn_0d_tvshows_rate
-- by their rating.
-- display: | title - rating | sorted in descending order by rating.

SELECT title, SUM(rate) AS 'rating'
FROM tv_show_ratings
	INNER JOIN tv_shows
	ON show_id = id
GROUP BY show_id
ORDER BY SUM(rate) DESC;
