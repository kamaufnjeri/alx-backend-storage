-- create table users with columns
-- id not null autoincrement unique primary key integer
-- email string(255) not null unique
-- name string(255)
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(id)
);