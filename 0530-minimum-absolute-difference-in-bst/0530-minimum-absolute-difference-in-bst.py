# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return float('inf')
        # else:
        #     if root.left and root.right:
        #         curr = min(abs(root.val - root.left.val), abs(root.val - root.right.val))
        #         return min(curr, min(self.getMinimumDifference(root.left), self.getMinimumDifference(root.right)))
        #     elif root.left and not root.right:
        #         return min(abs(root.val - root.left.val), self.getMinimumDifference(root.left))
        #     elif not root.left and  root.right:
        #         return min(abs(root.val - root.right.val), self.getMinimumDifference(root.right))
        #     else:
        #         return float('inf')
        
        def traverse(root, lst):
            if root:
                lst.append(root.val)

                traverse(root.left, lst)
                traverse(root.right, lst)        


            return lst
        vals = traverse(root, [])
        vals.sort()
        print(vals)
        dif = float('inf')
        for i in range(1, len(vals)):
            if vals[i] - vals[i - 1] < dif:
                dif = vals[i] - vals[i - 1]
        return dif

