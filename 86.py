# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #Bad Case1:
        if head is None:
            return None
        #Bad Case2:
        if head.next is None:
            return head
        
        index = head
        bigger_index, less_index = None, None
        #while index:
        #    print(index.val)
        #    index = index.next
        while index:
            if index.val >= x:
                if bigger_index is None:
                    bigger_index = index
                    bigger_head = index
                    #print('1', bigger_index.val)
                else:
                    bigger_index.next = index
                    bigger_index = index
                    #print('2', bigger_index.val)
            if index.val < x :
                if less_index is None:
                    less_index = index
                    less_head = index 
                    #print('3', less_index.val)
                else:
                    less_index.next = index
                    less_index = index
                    #print('4', less_index.val)
            index = index.next
       
        if less_index is None or bigger_index is None:
            return head
           
        bigger_index.next = None
        less_index.next = None
        index1 = less_head
        index2 = less_head.next
        while index2:
            #print(index1.val)
            index1 = index1.next
            index2 = index2.next
        
        index1.next = bigger_head
        
        return less_head
