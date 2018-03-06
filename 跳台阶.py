# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# -*- coding:utf-8 -*-
class Solution:#递归复杂度太大
    def jumpFloor(self, number):
        # write code here
        if number<0:
            return -1
        if number==1 or number==2:
            return number
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

class Solution:  #循环代替递归
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        c = 3
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c