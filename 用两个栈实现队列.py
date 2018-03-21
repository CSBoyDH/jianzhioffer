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
    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    # @return an boolean
    def empty(self):
        return len(self.inStack) + len(self.outStack) == 0