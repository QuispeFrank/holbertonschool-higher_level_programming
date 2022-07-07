-- 8. Cities of California
-- -------------------------
-- script that lists all the cities of California that 
-- can be found in your database.
-- Results is sorted in ascending order by cities.id

SELECT cities.id, cities.name FROM states, cities
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id;
