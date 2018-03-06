# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count=0;
        for i in range(0,32):
            if n&1:
                count=count+1
            n=n>>1
        return count
def num_of_one(num):
    '''
    count the num of "one" in num n
    bin():convert the num to binary string
    :param num: num num
    :return: the num of "one" in num
    '''
    if num >= 0:
        nbin = bin(num)
        return nbin.count('1')
    else:
        num = abs(num)
        nbin = bin(num-1)
        return 32 - nbin.count('1')
def num_of_one(num):
    nbin = bin(num & 0xffffffff)
    return nbin.count('1')