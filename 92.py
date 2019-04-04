# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_Link(self, link: ListNode):
            #实现链表的翻转
            if link is None:
                return []
            pre = link
            cur = pre.next
            pre.next = None
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #Bad Case 1:
        if head.next == None or m == n:
            return head
        
        index = head
        count = 0
        pre_start_index = None
        start_index = None
        end_index = None
        end_next_index = None
        while index:
            count += 1
            if count == (m-1):
                pre_start_index = index
            elif count == m:
                start_index = index
            elif count == n:
                end_index = index
                end_next_index = index.next
            index = index.next
        end_index.next = None
        temp = start_index
        start_index = self.reverse_Link(start_index)
        #index = bound_index[1]
        #while index:
        #    print(index.val)
        #    index = index.next
        if m == 1:
            head = start_index
        else:
            pre_start_index.next = start_index
        temp.next = end_next_index
        #index = head
        #while index:
        #    print(index.val)
        #    index = index.next
        
        return head
