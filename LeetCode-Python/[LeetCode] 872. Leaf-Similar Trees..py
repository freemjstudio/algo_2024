# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def visit_node(node, route):
            # Check if the node is leaf node
            if node.left == None and node.right == None:
                route.append(node.val)
                return route
            if node.left:
                visit_node(node.left, route)
            if node.right:
                visit_node(node.right, route)

            return route

        route1 = visit_node(root1, [])
        route2 = visit_node(root2, [])
        return (route1 == route2)
