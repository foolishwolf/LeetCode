# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        mt = TreeNode(None)
        if t1 == None and t2 == None:
            mt = None
        elif t1 != None and t2 == None:
            mt = t1
        elif t1 == None and t2 != None:
            mt = t2
        else:
            mt.val = t1.val + t2.val
            mt.left = self.mergeTrees(t1.left, t2.left)
            mt.right = self.mergeTrees(t1.right, t2.right)
        return mt