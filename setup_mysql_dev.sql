-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS 'prueba'@'localhost' IDENTIFIED BY '1_2_3_4_5_6_7_8_9_aSdFgHj_K_L';
GRANT SELECT ON `performance_schema`.* TO 'prueba'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'prueba'@'localhost';
