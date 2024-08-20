-- https://school.programmers.co.kr/learn/courses/30/lessons/273711
-- 다시 풀기 ! 

SELECT b.ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO a
JOIN ITEM_TREE b ON a.ITEM_ID = b.ITEM_ID 
WHERE b.PARENT_ITEM_ID IN (
    SELECT ITEM_ID
    FROM ITEM_INFO 
    WHERE RARITY = 'RARE'
) 
ORDER BY a.ITEM_ID DESC
