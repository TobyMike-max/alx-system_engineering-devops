-- Setup holberton mysql users on web servers 01 and 02
CREATE USER 
	IF NOT EXISTS 'holberton_user'@'localhost'
	IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT 
	ON *.*
	TO 'holberton_user'@'localhost';


CREATE DATABASE
	IF NOT EXISTS `tyrell_corp`;
CREATE TABLE
	IF NOT EXISTS `tyrell_corp`.`nexus6` (`id` INT, name VARCHAR(256));
INSERT INTO 
	`tyrell_corp`.`nexus6` (`id`, `name`)
	VALUES ('Koletin');
GRANT SELECT
	ON `tyrell_corp`.`nexus6`
	TO 'holberton_user'@'localhost';
CREATE USER
	IF NOT EXISTS 'replica_user'@'%'
	IDENTIFIED BY 'betty';
GRANT SELECT
	ON `mysql`.`user`
	TO 'holberton_user'@'localhost';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'replica_user'@'%';
