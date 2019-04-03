# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #Bad Case 1
        if head is None:
            return None
        
        pre = head
        dict1 = {}
        dict1[pre.val] = 1
        cur = head.next
        while cur:
            if cur.val in dict1.keys():
                pre.next = cur.next
            else:
                dict1[cur.val] = 1
                pre = pre.next
            cur = cur.next
           
        return head
