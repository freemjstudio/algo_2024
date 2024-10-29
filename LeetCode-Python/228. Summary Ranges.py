# https://leetcode.com/problems/summary-ranges/

"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"] # 이건 정렬된 상태이다. 각각의 숫자는 정확히 하나의 구간 안에 속해야 한다. 
0, 1, 2, 
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


"""
from typing import List 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        
        def formatter(s, e):
            return f"{s}->{e}"
            
        # 예외처리    
        if not nums:
            return []

        start = nums[0]
        
        for i in range(0, len(nums)-1): 
            if nums[i]+1 == nums[i+1]:
                continue
            else:
                if nums[i] == start:
                    result.append(str(nums[i]))
                    start = nums[i+1]
                else: 
                    result.append(formatter(start, nums[i]))
                    start = nums[i+1]
        end = nums[-1]
        if start == end:
            result.append(str(end))
        else: 
            result.append(formatter(start, end))
        return result 
