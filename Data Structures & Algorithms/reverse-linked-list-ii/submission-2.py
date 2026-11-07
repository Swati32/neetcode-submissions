# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        '''
        Before reversal begins:
        left_anchor (1) -> [2] -> [3] -> [4] -> [5]
                            ↑
                reversed_tail (and curr)

        After reversing [2, 3, 4]:
        reversed_head (prev)      reversed_tail       curr (right_anchor)
              ↓                   ↓                      ↓
            [4]  ->  [3]  ->    [2]                    [5]
        '''
        
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        left_anchor = dummy

        for i in range(left-1):
            left_anchor = left_anchor.next

        reversed_tail = left_anchor.next
        
        reversed_head = None
        curr = reversed_tail    
        

        for i in range(right - left + 1):
            temp = curr.next 
            curr.next = reversed_head
            reversed_head = curr
            curr = temp 
        
        right_anchor = curr
        left_anchor.next = reversed_head
        reversed_tail.next = right_anchor

        return dummy.next