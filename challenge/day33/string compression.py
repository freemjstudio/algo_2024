# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""
from typing import List 

# 로직 상관없이 구현하기 
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         answer = []
#         # 추가적인 space를 쓰지 말아야 함! set() 도 따라서 사용하면 안될듯 
#         alphabets = set(chars)
#         for ch in alphabets:
#             n = chars.count(ch)
#             if n == 1: 
#                 answer.append(ch)
#                 continue 
#             else: 
#                 answer.append(ch)
#                 if n < 10:
#                     answer.append(str(n))
#                 else: # 두자릿수 이상 
#                     n = str(n)
#                     for x in n:
#                         answer.append(x)
            
#         return len(answer)

# 문제 조건에 따라 풀기 
# chars 도 검사를 하고 있음 
class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = ""
        # 추가적인 space를 쓰지 말아야 함! set() 도 따라서 사용하면 안될듯 
        alphabets = set(chars)
        for ch in alphabets:
            n = chars.count(ch)
            if n == 1: 
                answer += ch 
                continue 
            else: 
                answer += ch
                answer += str(n) 
            
        return len(answer)

# TEST CASE 1 
sol = Solution()
chars1 = ["a","a","b","b","c","c","c"]
tc1 = sol.compress(chars1)
print("TESTCASE 1:", tc1)

# TEST CASE 2
sol = Solution()
chars2 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
tc2 = sol.compress(chars2)
print("TESTCASE 2:", tc2)
