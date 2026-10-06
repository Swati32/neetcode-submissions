class Node:
    def __init__(self, key = 0, value = 0, prev = None, next = None):
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

    def remove(self, node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
        
    def insert(self, node):
        temp = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev = temp
        temp.next = node
        
    def get(self, key: int) -> int:
        if self.cache and key in self.cache:
            node = self.remove(self.cache[key])
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cache and key in self.cache:
            node = self.remove(self.cache[key])
            node.value = value
            self.insert(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.remove(self.head.next)
            del self.cache[lru.key]
        
            
        
