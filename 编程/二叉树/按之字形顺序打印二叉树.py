# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印
# ，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其
# 他行以此类推。
class Solution:
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        lefttoright=False
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if lefttoright:
                curvalues.reverse()
            if curvalues:
                result.append(curvalues)
            level=nextlevel
            lefttoright=not lefttoright
        return result