-- 10. Genre ID by show
-- ----------------------
-- Script that lists all shows contained in hbtn_0d_tvshows.
-- display: |tv_shows.title - tv_show_genres.genre_id| sorted
--          in ascending order by: title, genre_id.

SELECT title, genre_id
FROM tv_show_genres INNER JOIN tv_shows
ON show_id = id
ORDER BY title, genre_id;
