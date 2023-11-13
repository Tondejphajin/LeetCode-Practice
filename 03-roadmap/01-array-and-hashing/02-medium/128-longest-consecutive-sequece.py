def longestConsecutive(nums):
    numsSet = set(nums)
    longest = 0

    for num in numsSet:
        if num - 1 not in numsSet:
            count = 1
            while num + 1 in numsSet:
                count += 1
                num = num + 1
            longest = max(longest, count)

    return longest


nums = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))
