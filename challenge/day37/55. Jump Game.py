# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

"""
You are given an integer array nums. 
You are initially positioned at the array's first index,
 and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List

# 문제 이해를 잘 못했었음 
# 최대 2만큼 뛴다 -> 0, 1, 2만큼 뛸 수 있다.
# Greedy 알고리즘 : 주어진 배열에서 가장 멀리 뛸 수 있는 인덱스를 확인한다 

class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        
    
        return True 

# Edge Case
nums = [2, 0, 0]
solution = Solution()
print(solution.canJump(nums=nums))

nums = [2,5,0,0]
olution = Solution()
print(solution.canJump(nums=nums))


