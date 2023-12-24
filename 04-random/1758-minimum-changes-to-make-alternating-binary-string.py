class Solution:
    def minOperations(self, s: str) -> int:
        # pattern 1 => 01010101010101
        # pattern 2 => 10101010101010

        pattern_1 = 0
        pattern_2 = 0

        for i in range(0, len(s)):
            if s[i] == "0" and i % 2 == 0 or s[i] == "1" and i % 2 == 1:
                pattern_1 += 1

            if s[i] == "1" and i % 2 == 0 or s[i] == "0" and i % 2 == 1:
                pattern_2 += 1

        return min(pattern_1, pattern_2)
