# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # elif not root.left and not root.right:
        #     return True
        # elif not root.left or not root.right:
        #     return False
        # elif root.left.val != root.right.val:
        #     return False
        # return self.isSymmetric(root.left) and self.isSymmetric(root.right)
        return self.isMirror(root, root)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False           
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)