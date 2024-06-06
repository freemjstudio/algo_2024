# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverse(self, left_node, right_node): 
        if left_node == None and right_node:
            return False 
        if left_node and right_node == None:
            return False 
        if left_node == None and right_node == None: # NoneType Err 
            return True 
        # 루트의 왼쪽 자식 노드와 오른쪽 자식 노드의 값을 비교하기 
        a = self.traverse(left_node.left, left_node.right) # left 
        b = self.traverse(right_node.left, right_node.right) # right 
        return a and b 
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.traverse(root.left, root.right)
