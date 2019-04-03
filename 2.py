# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l2_iter = l2.next
        l1_iter = l1.next
        carry = 0
        tmp = l1.val + l2.val
        if tmp >= 10:
            carry = 1
        l3 = ListNode(tmp%10)
        tmp = 0
        l3_iter = l3
        if l2_iter is None and l1_iter is None and (carry == 1):
            l3.next = ListNode(1)
        while True:
            if l1_iter is None and  l2_iter is None and carry == 0:
                break
            if l1_iter is not None:
                tmp = l1_iter.val
                l1_iter = l1_iter.next
            if l2_iter is not None:
                tmp += l2_iter.val
                l2_iter = l2_iter.next
            tmp += carry
            carry = 0
            sum1 = tmp % 10
            if tmp >= 10:
                carry = 1
            tmp = 0
            l3_iter.next = ListNode(sum1)
            l3_iter = l3_iter.next
        
        l3_iter = l3
        list1 = []
        while l3_iter is not None:
            list1.append(l3_iter.val)
            l3_iter = l3_iter.next
        return list2
