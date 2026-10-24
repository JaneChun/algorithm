# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        odd_list_head = head
        even_list_head = head.next

        odd_list_cur = odd_list_head
        even_list_cur = even_list_head

        cur = head.next.next
        number = 3
        
        while cur:
            if number % 2 == 1:
                odd_list_cur.next = cur
                odd_list_cur = odd_list_cur.next
            else:
                even_list_cur.next = cur
                even_list_cur = even_list_cur.next
            cur = cur.next
            number += 1
        
        even_list_cur.next = None
        odd_list_cur.next = even_list_head

        return odd_list_head
        