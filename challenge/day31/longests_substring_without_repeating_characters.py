# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

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