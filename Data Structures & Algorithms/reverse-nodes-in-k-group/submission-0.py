# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Check if there are at least k nodes left
        curr = head
        for _ in range(k):
            if not curr:
                return head  # Fewer than k nodes: leave as is!
            curr = curr.next

        prev, node = None, head
        for _ in range(k):
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        head.next = self.reverseKGroup(curr, k)

        return prev
        