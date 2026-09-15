class Node:
    def __init__(self, key = 0, value=0,prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert_node(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove_node(lru)
            del self.cache[lru.key]
        
