from typing import List 

# https://leetcode.com/problems/koko-eating-bananas/

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        MAX_K = max(piles)
        answer = MAX_K 
        
        def check_eatable(piles, k):
            cnt = 0 
            for p in piles: 
                cnt += p // k 
                if (p % k) != 0:
                    cnt += 1
            if cnt > h:
                return False 
            return True 

        left, right = 1, MAX_K
        while left <= right:
            mid = (left + right) // 2 # 이 mid 값으로 minimum k 값을 찾는다. 
            
        
            if check_eatable(piles, mid):
                answer = min(mid, answer)
                right = mid - 1
            else: 
                left = mid + 1

        return answer 

piles = [3,6,7,11]

h = 8

# Output: 4

s = Solution()
answer = s.minEatingSpeed(piles=piles, h=h)
print(answer)