# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 10**4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict

# frozen set 을 사용할 수 없음 -> dddddg, dggggg 의 경우 같은 anagram 으로 인식하기 때문
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        str_dict = defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            str_dict[k].append(s)

        answer = [v for v in str_dict.values()]
        return answer

## TEST CODE
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = s.groupAnagrams(strs)
print(result)

