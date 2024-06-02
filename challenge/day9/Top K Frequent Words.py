# https://leetcode.com/problems/top-k-frequent-words/description/
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        words_cnt = Counter(words)
        answer = [w[0] for w in sorted(words_cnt.items(), key=lambda x:(-x[1], x[0]))]
        
        return answer[:k]