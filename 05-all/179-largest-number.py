import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        sorted(iterable, key=key, reverse=reverse)
        key=functools.cmp_to_key()):

        Return -1: This indicates that the first argument is considered "less than" the second argument.
        In sorting terms, it means the first argument should appear before the second in the sorted sequence.

        Return 0: This indicates that the first argument is considered "equal to" the second argument in terms of sorting order.
        Because sorted() in Python is stable,this effectively means their original order is preserved.

        Return 1: This indicates that the first argument is considered "greater than" the second argument.
        The first argument should appear after the second in the sorted sequence.
        """

        nums = list(map(lambda num: str(num), nums))

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0

        res = sorted(nums, key=functools.cmp_to_key(compare))

        return str(int("".join(res)))
