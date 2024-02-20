import heapq
from typing import List


# O(nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a maxHeap
        # pop until get the answer
        # return the answer

        maxHeap = []
        heapq.heapify(maxHeap)
        for num in nums:
            heapq.heappush(maxHeap, -1 * num)

        res = maxHeap[0]
        while k >= 1:
            res = heapq.heappop(maxHeap) * -1
            k -= 1

        return res
