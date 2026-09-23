class ListNode:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next
        

class MyHashSet:

    def __init__(self):
        self.capacity = 100000
        self.buckets = [ListNode(-1) for _ in range(self.capacity)]

    def hash(self, key) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        cur = self.buckets[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return 
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.buckets[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
               cur.next = cur.next.next
               return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.buckets[self.hash(key)]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)