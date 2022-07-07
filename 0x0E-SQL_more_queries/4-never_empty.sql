-- 4. ID can't be null
-- ---------------------
-- script that creates the table id_not_null on your MySQL server.
-- id_not_null description:
-- 	id INT default value 1
--	name VARCHAR(256)
-- If the table id_not_null already exists, it does nothing.

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
