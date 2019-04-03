# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #Bad Case1
        if head == None:
            return None
        #Bad Case2
        if k == 0:
            return head
        #Bad Case3
        if head.next == None:
            return head
        #统计链表的节点个数
        index = head
        count = 0
        while index:
            count += 1
            index = index.next  
        
        for i in range(k%count):
            #找到尾部非空节点
            pre = head
            cur = head.next
            while cur.next:
                pre = pre.next
                cur = cur.next
            #print(pre.val)
            #print(cur.val)
            pre.next = None
            cur.next = head
            head = cur
            #index = head
            #while index:
            #    print(index.val)
            #    index = index.next
        
        return head
            
