# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
# 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum<3:#至少由两个数组成
            return []
        begin = 1
        end = 2
        middle = (tsum+1)/2#由于至少两个数，起始数不可能大于一半
        curSum = begin+end
        output = []
        while begin <middle:
            if curSum==tsum:
                output.append(range(begin,end+1))
                end+=1  #从小到大遍历，所以窗口向右扩展
                curSum +=end
            elif curSum>tsum:
                curSum-=begin
                begin+=1
            else:
                end +=1
                curSum+=end
        return output
