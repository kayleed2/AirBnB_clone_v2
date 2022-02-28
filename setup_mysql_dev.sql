-- Creates a MySql server with
-- database hbnb_dev_db
-- user hbnb_dev (in localhost)
-- password of hbnb dev is hbnb_dev_pwd

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performa_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILGES;