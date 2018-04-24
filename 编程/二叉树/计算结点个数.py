class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def NodeNum(self, root):
        if root == None:
            return 0
        else:
            return 1+self.NodeNum(root.left)+self.NodeNum(root.right)

    def leave(self, root):  # 递归求叶子节点个数
        if root == None:
            return 0
        elif root.left ==None and root.right ==None:
            return 1
        else:
            return self.leave(root.left)+self.leave(root.right)