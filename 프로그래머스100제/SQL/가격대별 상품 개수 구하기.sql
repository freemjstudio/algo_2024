-- https://school.programmers.co.kr/learn/courses/30/lessons/131530

SELECT MIN(PRICE) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE HAVING PRICE
ORDER BY PRICE_GROUP ASC