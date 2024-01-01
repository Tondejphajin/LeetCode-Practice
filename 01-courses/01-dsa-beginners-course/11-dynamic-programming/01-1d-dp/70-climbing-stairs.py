class Solution:
    def climbStairs(self, n: int) -> int:
        one_step = 1
        two_step = 1

        i = 1
        while i <= (n - 1):
            tmp = one_step
            one_step = one_step + two_step
            two_step = tmp
            i += 1

        return one_step
