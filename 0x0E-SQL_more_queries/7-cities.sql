-- 7. Cities table
-- -----------------
-- script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
-- cities description:
-- 	id INT unique, auto generated, not null and is a primary key
--	name VARCHAR(256) not null
--	state_id INT, not null, FOREIGN KEY to id of the states table
-- If the table states already exists, it does nothing.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
