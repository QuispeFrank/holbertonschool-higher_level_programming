-- 6. States table
-- -----------------
-- script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
-- 	id INT unique, auto generated, not null and is a primary key
--	name VARCHAR(256) not null
-- If the table states already exists, it does nothing.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
