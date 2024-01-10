class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: node

        # init dummy node
        self.dummyLeft = Node(0, 0)
        self.dummyRight = Node(0, 0)

        # connect dummy node
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def removeNode(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insertNode(self, node):
        dummyRight = self.dummyRight
        prevDummyRight = dummyRight.prev

        prevDummyRight.next = node
        node.prev = prevDummyRight

        dummyRight.prev = node
        node.next = dummyRight

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the double linked list
            lru = self.dummyLeft.next
            self.removeNode(lru)
            # remove from the cache (hashmap)
            del self.cache[lru.key]
