# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        head = ListNode()
        cur = head
        while a and b:
            if a.val < b.val:
                next_node = a.next
                cur.next = a
                cur = a
                a = next_node
            else:
                next_node = b.next
                cur.next = b
                cur = b
                b = next_node
        if not a:
            cur.next = b
        if not b:
            cur.next = a
        return head.next    