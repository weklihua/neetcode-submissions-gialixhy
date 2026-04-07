# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, a, b):
        dummy = ListNode()
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
                tail = tail.next
                
            else:
                tail.next = b
                b = b.next
                tail = tail.next
                
        if a:
            tail.next = a
        if b:
            tail.next = b
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self.merge(a, b))
            lists = merged_list
        return lists[0] if lists else None






