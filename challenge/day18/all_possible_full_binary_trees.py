# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        answer = []
        
        # root 홀수 idx//2, 짝수 idx//2-1
        def make_tree(temp_tree, idx):
            if temp_tree.count(0) == 7:
                answer.append(temp_tree)
                return
            if idx % 2 == 1: # 홀수 
                root_idx = idx//2
                if temp_tree[root_idx] == 0:
                    temp_tree.append(0)
                    make_tree(temp_tree, idx+1)
                    temp_tree.pop()
                    temp_tree.append(None)
                    make_tree(temp_tree, idx+1)
                    temp_tree.pop()
            else: 
                root_idx = idx//2-1
                if temp_tree[root_idx] == 0:
                    temp_tree.append(0)
                    make_tree(temp_tree, idx+1)
                    temp_tree.pop()
                    temp_tree.append(None)
                    make_tree(temp_tree, idx+1)
                    temp_tree.pop()
            
        
        return answer 