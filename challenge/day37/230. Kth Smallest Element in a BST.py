# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional 

import heapq 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = []
        heapq.heapify(queue)

        """
        힙에 모든 노드를 넣고 k-1 번만큼 heap에서 pop 시켜준다. 
        """

        # heappop 
        for _ in range(k-1):
            answer = heapq.heappop(queue)
        return answer 