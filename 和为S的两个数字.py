# 输入一个递增排序的数组和一个数字S，
# 在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S
# ，输出两个数的乘积最小的。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        output=[]
        minmut = 0xffffff
        for i in range(0,len(array)):
            if i+1<len(array):
                if (tsum-array[i]) in array[i+1:]:
                    if array[i]*tsum-array[i]<minmut:
                        minmut = array[i]*tsum-array[i]
                        output=[]
                        output.append(array[i])
                        output.append(tsum-array[i])
        return output

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ls = []
        if not isinstance(array, list):
            return ls
        for i, v in enumerate(array):
            for v1 in array[i:]:
                if (v + v1) == tsum:
                    ls.append([v, v1])
        if ls:
            return ls[0]
        else:
            return ls