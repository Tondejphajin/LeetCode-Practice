def maxSubarraySumCircular(nums) -> int:
    globMax, globMin = nums[0], nums[0]
    curMax, curMin = 0, 0
    total = 0

    for i, n in enumerate(nums):
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        total += n
        globMax = max(curMax, globMax)
        globMin = min(curMin, globMin)

        print(curMax, curMin, total, globMax, globMin)

    return max(globMax, total - globMin) if globMax > 0 else globMax


nums = [5, -3, 5]
print(maxSubarraySumCircular(nums))
