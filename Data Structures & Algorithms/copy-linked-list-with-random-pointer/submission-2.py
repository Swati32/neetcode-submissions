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
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        while curr:
            new_node = curr.next
            new_node.random = curr.random.next if curr.random else None
            curr = new_node.next
        
        
        curr, new_head = head, head.next
        while curr:
            clone = curr.next
            curr.next = clone.next
            clone.next = clone.next.next if clone.next else None
            curr = curr.next
        
        return new_head


