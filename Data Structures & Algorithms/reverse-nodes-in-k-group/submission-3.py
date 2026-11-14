# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Check if there are at least k nodes left
        next_head = head
        for _ in range(k):
            if not next_head:
                return head
            next_head = next_head.next
        
        prev = None
        curr = head

        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(next_head, k)

        return prev