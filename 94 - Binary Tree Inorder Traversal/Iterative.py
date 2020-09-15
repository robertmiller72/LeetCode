# 36ms, 14MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = []
        curr = root
        finals = []
        
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if not stack:
                    return finals
                curr = stack.pop()
                finals.append(curr.val)
                curr = curr.right
        