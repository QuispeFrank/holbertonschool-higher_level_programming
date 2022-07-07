-- 3. Always a name
-- ------------------
-- script that creates the table force_name on your MySQL server.
-- force_name description:
-- 	id INT
--	name VARCHAR(256) not null.
-- If the table force_name already exists, it does nothing.

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
