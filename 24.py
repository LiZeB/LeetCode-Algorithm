# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(None)
        pre.next = head
        result_list = pre
        while head and head.next:
            pre.next, head.next.next, head.next = head.next, head, head.next.next
            pre = head
            head = head.next
        return result_list.next
