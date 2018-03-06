# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        for index, value in enumerate(s):
            if s.count(value) == 1:
                return index

a = Solution()
print(a.FirstNotRepeatingChar('google'))