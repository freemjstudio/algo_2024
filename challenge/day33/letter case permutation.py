# https://leetcode.com/problems/letter-case-permutation/description/
"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""

from typing import List 

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        n = len(s)
        
        def backtracking(idx, n, word):
            if idx == n:
                answer.append(word)
                # print(word)
                return 
            now = s[idx] 
            if now.isnumeric():
                word += now
                backtracking(idx+1, n, word)
            else:
                # lowercase
                temp = word
                low = now.lower()
                temp += low
                backtracking(idx+1, n, temp)
                # uppercase
                temp = word
                up = now.upper()
                temp += up
                backtracking(idx+1, n, temp)

        backtracking(0, n, "")
        return answer 



# Test Case
sol = Solution()
s = "a1b2"
result = sol.letterCasePermutation(s)
print(result)