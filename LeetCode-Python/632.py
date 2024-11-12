"""
632. Smallest Range Covering Elements from K Lists
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
"""

# nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

from types import List 
import heapq 

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = [(num[0], row_idx, 0) for row_idx, num in enumerate(nums)]
        heapq.heapify(min_heap)
        # for row_idx, num in enumerate(nums):
        #     value = num[0]
        #     heapq.heappush(min_heap, (value, row_idx, 0))

        max_val = max(num[0] for num in nums)
        min_val = min_heap[0][0] # 최소 힙의 성질을 이용해서 가장 작은 값 찾기 
        answer = [min_val, max_val]
    
        # min_heap 의 길이가 nums 와 같다 -> 각 리스트에서 1개 이상 포함되어 있음 
        while len(min_heap) == len(nums):
            # Range 의 최소값 , 해당 값을 가져온 List 번호, 범위에 몇개의 List Val 이 들어가는지 확인 용 
            min_val, row_idx, count = heapq.heappop(min_heap)
                
            if count + 1 < len(nums[row_idx]): # out of index error 방지 
                new_val = nums[row_idx][count+1]
                heapq.heappush(min_heap, (new_val, row_idx, count+1))
                max_val = max(max_val, new_val)
                min_val = min_heap[0][0]
                # Update Range : Finding the smallest range 
                if max_val - min_val < answer[1] - answer[0]:
                    answer[0], answer[1] = [min_val, max_val]

        return answer 
""""
Counter 를 사용한 풀이보다 heapq 가 자체적으로 정렬해주니까 코드 구현이 더 쉬운것 같다. 
"""

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
s = Solution()
answer = s.smallestRange(nums)

