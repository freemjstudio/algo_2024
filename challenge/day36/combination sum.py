# https://leetcode.com/problems/combination-sum/description/?envType=study-plan-v2&envId=top-interview-150
"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
from typing import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        candidates.sort() # 정렬하기 
        
        # backtracking 
        def backtracking(start_idx:int, target:int, path: List[int]):
            if target < 0: # 현재 조합(path)은 target을 만들 수 없는 경우 
                return 
            if target == 0:
                answer.append(path.copy())
                return 
            
            for i in range(start_idx, len(candidates)):
                path.append(candidates[i])
                backtracking(i, target - candidates[i], path)
                path.pop() # 다시 삭제하기 

        backtracking(0, target, [])
        return answer 
    
### test case 1
candidates = [2,3,6,7]
target = 7

sol = Solution()
answer = sol.combinationSum(candidates, target)
print(answer)