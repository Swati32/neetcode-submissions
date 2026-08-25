# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None 
        curr =  slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        reverse_head = prev
        while head and reverse_head:
            temp = head.next
            head.next = reverse_head
            head = temp

            temp = reverse_head.next
            reverse_head.next = head
            reverse_head = temp



        