-- 13. Number of shows by genre
-- ------------------------------
-- Script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
-- display: | genre   number_of_shows | sorted in descending
--          order by the number of shows linked.

SELECT name AS 'genre', COUNT(genre_id) AS 'number_of_shows'
FROM tv_show_genres INNER JOIN tv_genres
ON id = genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
