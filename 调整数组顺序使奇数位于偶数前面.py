# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        ans=[]
        for i in range(0,len(array)):
            if array[i]%2==1:
                ans.append(array[i])
        for i in range(0,len(array)):
            if array[i]%2==0:
                ans.append(array[i])
        return ans
a = Solution()
print(a.reOrderArray([1,2,3,4,5,6,7]))
class Solution:
    def reOrderArray(self, array):
        # write code here
        start = 0
        end = len(array)-1
        while start<end:
            while array[start]%2==1:
                start = start+1
            while array[end]%2==0:
                end = end -1
            if start<end:
                tmp = array[start]
                array[start] = array[end]
                array[end] = tmp
                start = start+1
                end = end -1
        return array