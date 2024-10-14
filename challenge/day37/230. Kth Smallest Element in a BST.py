# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = 0 

        return answer 