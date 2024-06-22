# https://leetcode.com/problems/container-with-most-water/

from typing import List

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        answer = 0 
        left, right = 0, n-1
        while left < right: 
            w = (right - left)
            h = min(height[left], height[right]) # 둘중에 작은 높이가 기준이 됨! 
            answer = max(answer, w*h)

            # 어느 조건에서 left += 1 혹은 right -= 1
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return answer 

# Test Code 
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = s.maxArea(height=height)
print(result)