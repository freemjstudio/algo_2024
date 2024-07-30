from typing import List
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/ß
# O(m+n)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        t = (n+m) # length of the merged array 

        left, right = 0, 0 # cursor for nums1, cursor for nums2
        merged_arr = []

        while left < n and right < m:
            if nums1[left] <= nums2[right]:
                merged_arr.append(nums1[left])
                left += 1
            else: 
                merged_arr.append(nums2[right])
                right += 1
        
        # 남은 숫자 
        if left < n: 
            merged_arr.extend(nums1[left:])
        if right < m:
            merged_arr.extend(nums2[right:])
            
        if len(merged_arr) % 2 == 0: # 짝수인 경우 
            mid = len(merged_arr)//2
            return (merged_arr[mid] + merged_arr[mid-1])/2 
        else: # 홀수인 경우 
            mid = len(merged_arr)//2 
            return merged_arr[mid]

# O(log(m+n))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        left, right = 0, n
        while left <= right:
            i = (right - left + 1) // 2 + left
            j = (n + m + 1) // 2 - i
            nums1_1 = nums1[i - 1] if i > 0 else -sys.maxsize - 1
            nums1_2 = nums1[i] if i < n else sys.maxsize
            nums2_1 = nums2[j - 1] if j > 0 else -sys.maxsize - 1
            nums2_2 = nums2[j] if j < m else sys.maxsize
            if nums1_1 > nums2_2:
                right = i - 1
            elif nums2_1 > nums1_2:
                left = i + 1
            else:
                leftMax = max(nums1_1, nums2_1)
                rightMin = min(nums1_2, nums2_2)
                if (n + m) % 2 != 0:
                    return leftMax
                else:
                    return (leftMax + rightMin) / 2.0

        return 0.0
