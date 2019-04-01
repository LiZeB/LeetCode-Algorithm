# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        def display_Link(link: ListNode):
            #链表的输出
            index = link
            while index:
                print(index.val)
                index = index.next

        #Bad Case 0
        temp = []
        for element in lists:
            if element != None:
                temp.append(element)
        lists = temp
        #Bad Case 1
        if lists == []:
            return []
        #Bad Case 2
        if len(lists) == 1:
            return lists[0]
            
        
        index_lists = []
        min_index = lists[0]
        min_Index = 0
        for i, element in enumerate(lists):
            index_lists.append(element)
            if (element is not None) and element.val < min_index.val:
                min_index = element
                min_Index = i
        #定义新链表并给第一个节点赋值
        head = ListNode(min_index.val)
        index = head
       
        index_lists[min_Index] = index_lists[min_Index].next
        if index_lists[min_Index] is None:
            index_lists.remove(index_lists[min_Index])
        
        while len(index_lists) > 1:
            min_index = index_lists[0]
            min_Index = 0
            for i, element2 in enumerate(index_lists):
                if (element2 is not None) and element2.val <= min_index.val:
                    min_index = element2
                    min_Index = i
            index.next = ListNode(min_index.val)
            index = index.next
            index_lists[min_Index] = index_lists[min_Index].next
            if index_lists[min_Index] is None:
                index_lists.remove(index_lists[min_Index])
            
        
        if len(index_lists) == 1 and index_lists[0] is not None:
            index.next = index_lists[0]
        #display_Link(head)
        
        return head
