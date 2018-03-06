# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.inStack.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        return self.outStack.pop()
