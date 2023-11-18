def threeSum(nums):
    nums = sorted(nums)
    result = []
    for i, v in enumerate(nums):
        if v > 0:
            continue

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            threeSum = v + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([v, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
