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
        arr = nums1 + nums2
        n = len(arr)
        arr.sort() 

        mid = n//2
        if n%2 == 0: # 짝수인 경우 
            
            return arr[mid]
        else: # 홀수인 경우 
            
            return arr[mid]
