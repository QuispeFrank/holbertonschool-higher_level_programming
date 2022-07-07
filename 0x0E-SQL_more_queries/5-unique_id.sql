-- 5. Unique ID
-- --------------
-- script that creates the table unique_id on your MySQL server.
-- unique_id description:
-- 	id INT default value 1 and it'll be unique
--	name VARCHAR(256)
-- If the table unique_id already exists, it does nothing.

CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
