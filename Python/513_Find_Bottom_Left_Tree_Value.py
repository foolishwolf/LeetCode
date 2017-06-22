# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.botLeftVal = None
        self.maxLevel = 1

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.botLeftVal = root.val
        self.find(1, root.left)
        self.find(1, root.right)
        return self.botLeftVal
            
    def find(self, level, node):
        if node == None:
            return 
        level += 1
        if level > self.maxLevel:
            self.maxLevel += 1
            self.botLeftVal = node.val
        self.find(level, node.left)
        self.find(level, node.right)
        return