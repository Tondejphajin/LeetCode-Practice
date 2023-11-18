class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l, r = 1, res

        while l <= r:
            k = (l + r) // 2

            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(pile / k)

            if totalHours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
