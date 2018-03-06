# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a = 0
        b = 1
        res = 1
        if n<2:
            return n
        for i in range(2,n):
            a = b
            b = res
            res = a+b
        return res
