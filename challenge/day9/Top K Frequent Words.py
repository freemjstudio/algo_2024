# https://leetcode.com/problems/top-k-frequent-words/description/
from collections import Counter
import heapq

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]: 
#         words_cnt = Counter(words)
#         answer = [w[0] for w in sorted(words_cnt.items(), key=lambda x:(-x[1], x[0]))]
        
#         return answer[:k]
    
from collections import Counter
import heapq
    
class WordCnt:
    def __init__(self, word:str, cnt:int):
        self.word = word
        self.cnt = 1
    
    def __lt__(self, other):
        if self.cnt == other.cnt: # cnt 같으면 word 순으로 정렬 
            return self.word > other.word 
        return self.cnt < other.cnt 

class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        words_cnt = Counter(words) # O(N) 의 extra 공간 사용 , word : WordCnt
        pq = [] # priority queue 
        heapq.heapify(pq)
        
        for word, cnt in words_cnt.items():
            heapq.heappush(pq, WordCnt(word, cnt)) 
            
            if len(pq) > k: # evict least count element 
                heapq.heappop(pq)
        
        # 알파벳 순 - min heap 이니까 (a, b, c .. 대로 정렬됨) 
        # 그대로 k개를 priority queue에서 heappop 하여 정렬한다. 
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(pq).word)
        
        return answer