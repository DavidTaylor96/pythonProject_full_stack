DROP TABLE companys;
DROP TABLE categorys;
DROP TABLE users;  
DROP TABLE accounts;


CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  account_name VARCHAR(255),
  amount FLOAT
);


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  account_id INT REFERENCES accounts(id)
);


CREATE TABLE categorys (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE companys (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  amount FLOAT,
  category_id INT REFERENCES categorys(id) ON DELETE CASCADE,
  account_id INT REFERENCES accounts(id) ON DELETE CASCADE
);