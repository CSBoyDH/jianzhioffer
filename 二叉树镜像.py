class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root != None:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)