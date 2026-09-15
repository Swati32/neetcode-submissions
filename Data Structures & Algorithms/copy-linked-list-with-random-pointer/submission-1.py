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
            return None

        # Step 1: Interweave copied nodes directly after original nodes
        # A -> B -> C becomes A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers to the copied nodes
        # The copy of curr is curr.next, and the copy of curr.random is curr.random.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Decouple the copied list and restore the original list
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            curr = curr.next
            copy.next = curr.next if curr else None

        return copy_head