CREATE USER 'holberton_user'@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;


CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id int,name varchar(64));
INSERT INTO nexus6 (id, name) VALUES (1, 'Leon');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@localhost;
FLUSH PRIVILEGES;


CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_pass';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@localhost;

CHANGE MASTER TO SOURCE_HOST='100.25.170.65', SOURCE_USER='replica_user', SOURCE_PASSWORD='replica_pass', SOURCE_LOG_FILE='mysql-bin.000001', SOURCE_LOG_POS=154;