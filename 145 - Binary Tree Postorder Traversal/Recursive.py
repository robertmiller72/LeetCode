# 32ms, 14MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if root:
            nodes += self.postorderTraversal(root.left)
            nodes += self.postorderTraversal(root.right)
            nodes.append(root.val)
        return nodes