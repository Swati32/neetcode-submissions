# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        if not lists:
            return None
        
        # Repeat pairwise merges until only 1 merged list remains
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                merged_list.append(self._mergeTwoLists(l1, l2))
            lists = merged_list
                
        return lists[0]

    def _mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            
            return dummy.next
   
        dummy = ListNode()
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        curr = dummy
        while min_heap:
            _ , i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                node.next = node.next.next
        
        return dummy.next
        '''

        def merge_two(l1:ListNode, l2:ListNode) -> ListNode:
            if not l1:
                return l2
            if not l2:
                return l1

            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2

            return dummy.next

        if not lists:
            return 
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                temp = merge_two(list1, list2)
                merged.append(temp)
            lists = merged

        return lists[0]
        





    


        