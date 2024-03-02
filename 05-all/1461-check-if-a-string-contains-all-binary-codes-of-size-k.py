class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        unique_code = set()

        for i in range(0, len(s) - k + 1):

            unique_code.add(s[i : i + k])

        return True if len(unique_code) == 2**k else False
