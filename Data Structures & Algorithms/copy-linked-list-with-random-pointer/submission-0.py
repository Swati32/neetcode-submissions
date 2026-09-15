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
        copy = {None:None}
        curr = head

        # now we have copies of all nodes, key is old node, value is new node
        while curr:
            copy[curr] = Node(curr.val) # make sure to create node
            curr = curr.next

        # we get copy of curr node, set next and random using copy
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random] 
            curr = curr. next
        
        return copy[head]

        
