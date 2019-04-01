# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        index1 = l1
        index2 = l2
        #Bad case
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        #定义新链表，给新链表的第一个节点赋值
        if l1.val >= l2.val:
            head = ListNode(l2.val)
            index2 = index2.next
        else:
            head = ListNode(l1.val)
            index1 = index1.next
        index3 = head
        
        while index1 and index2:
            if index1.val == index2.val:
                index3.next = ListNode(index1.val)
                index1 = index1.next
            elif index1.val > index2.val:
                index3.next = ListNode(index2.val)
                index2 = index2.next
            else:
                index3.next = ListNode(index1.val)
                index1 = index1.next
            index3 = index3.next           
        
        if index2:
            index3.next = index2
        else:
            index3.next = index1
            
        return head
