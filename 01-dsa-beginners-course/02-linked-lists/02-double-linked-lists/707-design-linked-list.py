class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0 and cur != self.right:
            return cur.val

        return -1

    def addAtHead(self, val: int) -> None:
        newNode, prevNode, nextNode = ListNode(val), self.left, self.left.next

        newNode.prev = prevNode
        newNode.next = nextNode

        prevNode.next = newNode
        nextNode.prev = newNode

    def addAtTail(self, val: int) -> None:
        newNode, lastNode, beforeLastNode = ListNode(val), self.right, self.right.prev

        newNode.prev, newNode.next = beforeLastNode, lastNode
        lastNode.prev = newNode
        beforeLastNode.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        firstNode = self.left.next

        while firstNode and index > 0:
            firstNode = firstNode.next
            index -= 1

        if firstNode and index == 0:
            prev, newNode, next = firstNode.prev, ListNode(val), firstNode

            prev.next = newNode
            next.prev = newNode

            newNode.prev, newNode.next = prev, next

    def deleteAtIndex(self, index: int) -> None:
        firstNode = self.left.next
        while firstNode and index > 0:
            firstNode = firstNode.next
            index -= 1

        if firstNode and index == 0 and firstNode != self.right:
            prev, next = firstNode.prev, firstNode.next

            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
