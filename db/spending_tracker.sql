DROP TABLE IF EXISTS companys;
DROP TABLE IF EXISTS categorys;
DROP TABLE IF EXISTS users;  


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  amount INT
);

CREATE TABLE categorys (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE companys (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  amount INT,
  category_id INT REFERENCES categorys(id)
  user_id INT REFERENCES users(id)
);