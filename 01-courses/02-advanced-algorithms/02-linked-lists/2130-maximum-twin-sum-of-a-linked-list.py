from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        maxSum = 0
        while prev and slow:
            pairSum = prev.val + slow.val
            maxSum = max(pairSum, maxSum)
            prev = prev.next
            slow = slow.next

        return maxSum
