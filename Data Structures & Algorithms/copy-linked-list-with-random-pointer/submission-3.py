"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        
        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = copy.next
        
        
        curr, new_head = head, head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = curr.next.next if curr.next else None
            curr = curr.next
        
        return new_head


