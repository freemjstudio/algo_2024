-- https://school.programmers.co.kr/learn/courses/30/lessons/273712

SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO 
WHERE 1=1
AND ITEM_ID NOT IN (
    SELECT PARENT_ITEM_ID 
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IS NOT NULL
)
ORDER BY ITEM_ID DESC;

-- NOT IN 은 AND 연산을 진행한다. 
