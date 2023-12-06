def minSubArrayLen(target: int, nums: list[int]) -> int:
    l = 0
    sum = 0
    minLength = float("inf")

    for r in range(len(nums)):
        sum += nums[r]

        while sum >= target:
            minLength = min(minLength, r - l + 1)
            sum -= nums[l]
            l += 1

    return 0 if minLength == float("inf") else minLength


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
