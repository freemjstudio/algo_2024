# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)

        def traverse(node, depth):
            levels[depth] += node.val
            if node.left:
                traverse(node.left, depth + 1)
            if node.right:
                traverse(node.right, depth + 1)

        traverse(root, 1)

        max_level, max_val = -int(1e9), -int(1e9)
        for k, v in levels.items():
            if v > max_val:
                max_val = v
                max_level = k
        return max_level
