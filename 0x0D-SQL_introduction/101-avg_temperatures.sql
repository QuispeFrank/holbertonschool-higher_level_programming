-- 18. Temperatures #0
-- ---------------------
-- Write a script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC
