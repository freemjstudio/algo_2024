# https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=study-plan-v2&envId=leetcode-75

import heapq 

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        answer = 0  # total cost
        left_idx, right_idx = candidates, max(len(costs) - candidates, candidates)-1
        left_queue = costs[:left_idx]
        right_queue = costs[right_idx+1:]
        # make list to heap queue to get min cost 
        heapq.heapify(left_queue)
        heapq.heapify(right_queue)
        # to hire k workers 
        for session in range(k):
            # right_queue can be empty array (ex.3)
            if not right_queue or (left_queue and left_queue[0] <= right_queue[0]):
                answer += heapq.heappop(left_queue)
                if left_idx <= right_idx: # queue 를 슬라이딩 윈도우 처럼 한칸 조정하기 
                    heapq.heappush(left_queue, costs[left_idx])
                    left_idx += 1
                
            else: 
                answer += heapq.heappop(right_queue)
                if left_idx <= right_idx:
                    heapq.heappush(right_queue, costs[right_idx])
                    right_idx -= 1
            
            
        return answer 
        