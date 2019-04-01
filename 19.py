# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def reverse_Link(link: ListNode):
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
        
        def display_Link(link: ListNode):
            #链表的输出
            index = link
            while index:
                print(index.val)
                index = index.next
        
        link = reverse_Link(head)
        display_Link(link)
        
        #要删除的是首节点
        if n == 1:
            link = link.next
            return reverse_Link(link)
        #要删除的不是首节点
        index = link
        pre = link
        count = 0
        while index:
            count += 1
            if count == n:
                pre.next = index.next
                break
            pre = index
            index = index.next
        
        display_Link(link)
        link1 = reverse_Link(link)
        
        return link1
