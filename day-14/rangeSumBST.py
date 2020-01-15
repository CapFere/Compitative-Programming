# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return
        elif root.val >=L and root.val <=R:
            self.sum += root.val
            self.rangeSumBST(root.left,L,R)
            self.rangeSumBST(root.right,L,R)
        elif root.val <=L:
            self.rangeSumBST(root.right,L,R)
        else:
            self.rangeSumBST(root.left,L,R)   
        return self.sum