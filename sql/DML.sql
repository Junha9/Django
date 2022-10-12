CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age FROM users;

SELECT * FROM users;

SELECT rowid, first_name FROM users;

SELECT first_name, age FROM users ORDER BY age DESC;

SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

SELECT DISTINCT country FROM users
ORDER BY country;

SELECT DISTINCT first_name, country FROM users;

SELECT DISTINCT first_name, country FROM users
ORDER BY country ASC;

SELECT DISTINCT first_name FROM users
WHERE country = '제주특별자치도';

SELECT first_name, age, balance FROM users
WHERE age >= 30 and balance > 500000
ORDER BY age ASC;

SELECT first_name, last_name FROM users
-- WHERE first_name LIKE '%호%';
WHERE first_name LIKE '%준';

SELECT first_name, phone FROM users
WHERE phone LIKE '02%';

SELECT first_name, age FROM users
WHERE age LIKE '2_'
ORDER BY age ASC;

SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

SELECT first_name, country FROM users
WHERE country NOT IN ('강원도', '경기도');

SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30
LIMIT 30;

SELECT first_name, balance FROM users
ORDER BY balance DESC
LIMIT 10;

SELECT first_name, age FROM users
ORDER BY age ASC
LIMIT 5;

SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

SELECT country, COUNT(*) FROM users GROUP BY country;

SELECT last_name, COUNT(*) AS number_of_name
FROM users GROUP BY last_name
ORDER BY COUNT(*) DESC;

SELECT country, AVG(age) FROM users
GROUP BY country;

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES
  ('주나박', 29, '아이고배야'),
  ('다이소', 33, '장난이얌');

UPDATE classmates
SET name= '김철수한무두루미',
  address= '제주도'
WHERE rowid = 2;

DELETE FROM classmates WHERE rowid=3;

SELECT rowid, * FROM classmates;

DELETE FROM classmates
WHERE name LIKE '%한%';
