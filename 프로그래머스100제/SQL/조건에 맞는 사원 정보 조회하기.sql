-- https://school.programmers.co.kr/learn/courses/30/lessons/284527




SELECT a.SCORE, a.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL
FROM (
    SELECT EMP_NO, SUM(SCORE) as SCORE 
    FROM HR_GRADE
    WHERE YEAR = '2022'
    GROUP BY EMP_NO
) a JOIN HR_EMPLOYEES b 
ON a.EMP_NO = b.EMP_NO
WHERE a.SCORE = (
    SELECT MAX(SCORE) FROM (
        SELECT SUM(SCORE) as SCORE
        FROM HR_GRADE
        WHERE YEAR = '2022'
        GROUP BY EMP_NO
    ) max_score
)

-- 참고한 풀이 
WITH G_SCORE 
AS (
    SELECT EMPNO, sum(SCORE) as SCORE 
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT a.SCORE, a.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL 
FROM G_SCORE a 
JOIN HR_EMPLOYEES b 
ON a.EMP_NO = b.EMP_NO
WHERE score = (
    SELECT max(SCORE) 
    FROM G_SCORE
)