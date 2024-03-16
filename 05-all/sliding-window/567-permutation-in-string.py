from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        charCount1 = Counter(s1)
        charCount2 = Counter(s2[: len(s1)])  # Initial window based on the size of s1

        if charCount1 == charCount2:
            return True

        for i in range(len(s1), len(s2)):
            # Add new char to the current window
            charCount2[s2[i]] += 1
            # Remove one char from the left of the current window
            charCount2[s2[i - len(s1)]] -= 1

            # Remove keys with zero count to keep the counters equal in terms of keys present
            if charCount2[s2[i - len(s1)]] == 0:
                del charCount2[s2[i - len(s1)]]

            if charCount1 == charCount2:
                return True

        return False
