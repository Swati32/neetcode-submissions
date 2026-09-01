# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode()
        head = dummy
        heap = []

        for idx, l_head in enumerate(lists):
            if l_head:
                heapq.heappush(heap, (l_head.val, idx, l_head))

        while heap:
            l_head_val, idx, l_head = heapq.heappop(heap)
            head.next = l_head
            head = head.next

            if l_head.next:
                heapq.heappush(heap, (l_head.next.val, idx, l_head.next))
        
        return dummy.next
