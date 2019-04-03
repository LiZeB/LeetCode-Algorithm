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
        
        index = head
        dict1 = {}
        while index:
            if index.val not in dict1.keys():
                dict1[index.val] = 1
            else:
                dict1[index.val] += 1
            index = index.next
        
        pre = head
        cur = head.next
        while cur:
            if dict1[cur.val] > 1:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        
        #Bad Case2
        if dict1[head.val] > 1:
            head = head.next
        
        return head
