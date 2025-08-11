-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 1. Insert data into table
INSERT INTO
  articles (title, content, createdAt)
VALUES  
  ('hello', 'world', '2000-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES  
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

INSERT INTO
  articles (id, title, content, createdAt)
VALUES  
  (11, 'hello', 'world', DATE());

INSERT INTO
  articles (title, content, createdAt)
VALUES  
  ('hello', 'world', DATE());

-- 2. Update data in table
UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 1;

SELECT *
FROM articles
WHERE title LIKE 'hello%';

UPDATE articles
SET title = 'title'
WHERE title LIKE 'hello%';


-- 3. Delete data from table
DELETE FROM articles
WHERE id = 12;

DELETE FROM articles
WHERE title LIKE 'title%';

UPDATE articles
SET createdAt = Date()
where id = 15;

SELECT *
FROM articles
ORDER BY createdAt;

SELECT *
FROM articles
ORDER BY createdAt
LIMIT 2;

SELECT *
FROM articles
WHERE id in
  (SELECT id
  FROM articles
  ORDER BY createdAt
  LIMIT 2);


DELETE FROM articles
WHERE id in
  (SELECT id
  FROM articles
  ORDER BY createdAt
  LIMIT 2);