class ListNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.next = next
        self.value = value
class MyHashMap:

    def __init__(self):
        self.capacity = 100001
        self.buckets = [ListNode(-1) for _ in range(self.capacity)]

    def hash(self, key) -> int:
        return key % self.capacity      

    def put(self, key: int, value: int) -> None:
        cur = self.buckets[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        cur = self.buckets[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.buckets[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)