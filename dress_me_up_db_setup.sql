-- Sets up a database for Dress_Me_Up project

CREATE DATABASE IF NOT EXISTS dress_me_up_dev_db;

CREATE USER IF NOT EXISTS 'dress_me_up_dev'@'localhost'
IDENTIFIED BY 'dress_me_up_dev_pwd';

GRANT ALL PRIVILEGES ON dress_me_up_dev_db.* TO
'dress_me_up_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO
'dress_me_up_dev'@'localhost';

FLUSH PRIVILEGES;
