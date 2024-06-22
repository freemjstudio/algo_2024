SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO 
WHERE RARITY = 'LEGEND'

-- 물고기 종류 별 대어 찾기 
SELECT t1.ID, t2.FISH_NAME, t1.LENGTH
FROM (
SELECT ID, FISH_TYPE, LENGTH FROM FISH_INFO
GROUP BY FISH_TYPE HAVING MAX(LENGTH)
) t1
JOIN FISH_NAME_INFO t2 
ON t1.FISH_TYPE = t2.FISH_TYPE
ORDER BY ID ASC

