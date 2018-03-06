# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def Height(self, root):
        if root == None:
            return 0
        return max(self.Height(root.left), self.Height(root.right)) + 1

    def IsBalanced_Solution(self, root):
        # write code here
        if root == None:
            return True
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
        else:
            return False
class Solution(object):
    def Height(self, root):
        if root == None:
            return 0
        return max(self.Height(root.left), self.Height(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False