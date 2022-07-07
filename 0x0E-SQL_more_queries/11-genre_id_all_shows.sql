-- 11. Genre ID for all shows
-- ----------------------------
-- Script that lists all shows contained in hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL.
-- display: |tv_shows.title - tv_show_genres.genre_id| sorted
--          in ascending order by: title, genre_id.

SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON show_id = id
ORDER BY title, genre_id;

