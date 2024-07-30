# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""
Brute Force 풀이 
O(N**2)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 1
        
        # edge case 
        n = len(s)
        if n <= 1: 
            return len(s)

        left, right = 0, 1
        window = set(s[left])
        while left <= right and right < n: 
            if s[right] not in window: 
                window.add(s[right])
                right += 1
            else: 
                left += 1
                window = set(s[right])
            
            # update the result 
            answer = max(answer, len(window))
        
        return answer 
"""

 # Sliding Window 
 # O(N)  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        
        # character : int 
        info = dict()
        left_ptr = 0 
        
        # info = {'a':0, 'b':1, 'c':2}
        for right_ptr, char in enumerate(s): # a, 3 현재 left_ptr = 0
		        # 동일 문자가 두번 등장한 경우.
            if char in info and left_ptr <= info[char]:
                left_ptr = info[char] + 1 # left_ptr 은 3 으로 갱신 
            else:
                answer = max(answer, right_ptr - left_ptr + 1)
            info[char] = right_ptr # info = {'a':3, 'b':1, 'c':2}

        return answer 
    
"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

s = " "
sol = Solution()
ans = sol.lengthOfLongestSubstring(s=s)
print(ans)