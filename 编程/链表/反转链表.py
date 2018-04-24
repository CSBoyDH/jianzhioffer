# 输入一个链表，反转链表后，输出链表的所有元素。
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next=pHead
            pHead.next=None
            return newHead
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None: return None
        head = pHead
        pHead = pHead.next
        head.next = None
        while pHead!=None:
            next = pHead.next
            pHead.next = head
            head = pHead
            pHead = next
        return head

