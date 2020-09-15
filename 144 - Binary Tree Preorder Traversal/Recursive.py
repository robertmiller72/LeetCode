# 32ms, 13.8MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if root:
            nodes = [root.val]
            nodes += self.preorderTraversal(root.left)
            nodes += self.preorderTraversal(root.right)
        return nodes
        