# 一个链表中包含环，请找出该链表的环的入口结点。
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead==None or pHead.next==None or pHead.next.next==None:
            return None
        low=pHead.next
        fast=pHead.next.next
        while low!=fast:
            if fast.next==None or fast.next.next==None:#说明无环
                return None
            low=low.next
            fast=fast.next.next
        #如果走出上面这个循环说明有环，且fast = slow
        fast=pHead
        #找出环的入口
        while low!=fast:
            low=low.next
            fast=fast.next
        return fast