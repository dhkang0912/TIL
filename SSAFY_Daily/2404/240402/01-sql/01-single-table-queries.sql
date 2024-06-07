-- 01. Querying data
SELECT 
  LastName 
FROM 
  employees;

SELECT 
  LastName, FirstName
FROM 
  employees;

SELECT 
  *
FROM 
  employees;

SELECT 
  FirstName AS '이름'
FROM 
  employees;

SELECT
  Name, 
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;



-- 02. Sorting data
SELECT 
  FirstName AS '이름'
FROM 
  employees
ORDER BY
  FirstName ASC;

SELECT 
  FirstName AS '이름'
FROM 
  employees
ORDER BY
  FirstName DESC;

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City ASC;

SELECT
  Name, 
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering data
-- distinct == 중복제거
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- where 절이 아주 중요하다. 
-- 많이 쓰임, 조건을 거는 절
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';


SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';


SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  -- NULL의 경우 =이 아니라 is로 조건을 검
  Company IS NULL 
  -- 조건의 경우 논리연산자 사용
  OR Country = 'USA';


SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- Bytes >= 100000
  -- AND Bytes <= 500000;
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country = 'Canada'
  OR Country = 'Germany'
  OR Country = 'France';


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');


SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';


SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT
  7 ;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT
  3, 4 ;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 4 OFFSET 3;

-- 04. Grouping data
-- 평균, 최대, 최소 값 등 집계 함수와 함께 쓰임
SELECT
  Country, COUNT(*)
FROM 
  customers
GROUP BY
  Country ;


SELECT 
  Composer, AVG(Bytes) AS avgOFBytes
FROM
  tracks
GROUP BY
  Composer 
ORDER BY
  -- as로 바꿔준 키워드로 사용
  avgOFBytes DESC;


-- 그룹에 조건을 걸려면 having절을 써야함
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOFMinuite
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOFMinuite < 10;
