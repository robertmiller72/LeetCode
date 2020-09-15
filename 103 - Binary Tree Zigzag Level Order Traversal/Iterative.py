# 36ms, 13.8MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        curr = root
        layer = [root]
        answer = []
        flip = False
        
        while curr and layer:
            below = []
            for node in layer:
                if node.left:
                    below.append(node.left)
                if node.right:
                    below.append(node.right)
                    
            if not flip:
                answer.append([x.val for x in layer])
            else:
                answer.append([x.val for x in layer[::-1]])
                
            flip = not flip
            layer = below
        return answer