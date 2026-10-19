class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        # Initialize an array of dummy head nodes
        self.size = 1000
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        curr = self.buckets[idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
            
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        curr = self.buckets[idx].next
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        curr = self.buckets[idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next