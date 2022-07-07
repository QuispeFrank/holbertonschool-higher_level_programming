-- 9. Cities by States
-- ---------------------
-- script that lists all cities contained in the database. 
-- display: cities.id - cities.name - states.name
-- Results is sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE state_id = states.id;
