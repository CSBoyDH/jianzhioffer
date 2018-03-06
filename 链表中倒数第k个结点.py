# 输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k<=0 or head==None:
            return None
        count=0
        p=head
        while p!=None:
            count=count+1
            p=p.next
        if count<k:
            return None
        number=count-k+1
        cnt=0
        p=head
        while p!=None:
            cnt=cnt+1
            if cnt==number:
                return p
            p=p.next