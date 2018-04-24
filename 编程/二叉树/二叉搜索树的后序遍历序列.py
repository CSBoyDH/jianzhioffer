# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
#对于二叉搜索树后序遍历，最后一个元素为根结点，除过根结点，sequence可以分为两段。左半段比根小，
#右半段比根大，对于每一段都是同样的处理方式。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        if len(sequence) ==1 :
            return True
        return self.jugle(sequence,0,len(sequence)-1)
    def jugle(self,sequence,start,root):
        if start>=root:
            return True
        i = root
        while(i>start and sequence[i-1]>sequence[root]):
            i = i-1                    #找到左半段和右半段的分界点
        for j in range(start,i-1):
            if sequence[j]>sequence[root]: #判断是不是左半段都小于root
                return False
        return self.jugle(sequence,start,i-1) and self.jugle(sequence,i,root-1)