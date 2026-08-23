# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNodeWrapper:
    def __init__(self, node):
        self.node = node

    # This defines the '<' behavior for the heap
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode()
        minHeap = []
        cur = res

        for lst in lists:
            if list is not None:
                heapq.heappush(minHeap, HeapNodeWrapper(lst))
        

        while minHeap:
            min_node = heapq.heappop(minHeap)
            cur.next = min_node.node
            cur = cur.next

            if min_node.node.next:
                heapq.heappush(minHeap, HeapNodeWrapper(min_node.node.next))

        return res.next