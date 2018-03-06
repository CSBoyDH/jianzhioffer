# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base**exponent
class Solution:
    def Power(self, base, exponent):
        # write code here
        #if base<0.0000001 and base>-0.0000001:
         #   return 0;
        #else:
        if exponent==0:
            return 1;
        exp=abs(exponent)
        ans=1.0
        for i in range(0,exp):
            ans=ans*base
        if exponent>0:
            return ans;
        else :
            return 1/ans