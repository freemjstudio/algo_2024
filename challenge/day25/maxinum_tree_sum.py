# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

from typing import Optional

"""

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = -int(1e9)

        def dfs(root):
            nonlocal answer 

            if root is None: # node 
                return 0
            
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            
            answer = max(answer, root.val + left_max + right_max)
            
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return answer


#### Test Case 
# 답이 6이 나와야 함 

testcase = TreeNode(val= 1, left= TreeNode(val= 2, left= None, right= None), right= TreeNode(val= 3, left= None, right= None))
s = Solution()
answer = s.maxPathSum(root=testcase)
print(answer)