SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE &(SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
OR SKILL_CODE &(SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
ORDER BY ID 

-- 비트 연산에서 & 는 AND 연산으로 두 비트가 모두 1일때 결과가 1이됨. 
-- | OR 연산 으로 두 비트 중 하나라도 1이면 결과가 1이됨. 
-- ^ : XOR 두 비트가 다를 때 결과가 1이됨 
-- ~ NOT : 모든 비트를 반전시킨다. 