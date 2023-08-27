# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        elif not root.left and not root.right:
            return targetSum - root.val== 0
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
    # def helperSum(self, root: Optional[TreeNode], targetSum: int, total: int) -> bool:
    #     if not root:
    #         return False

    #     elif not root.left and not root.right:
    #         return targetSum == total + root.val
    #     else:
    #         return self.helperSum(root.left, targetSum, total + root.val) or self.helperSum(root.right, targetSum , total + root.val)