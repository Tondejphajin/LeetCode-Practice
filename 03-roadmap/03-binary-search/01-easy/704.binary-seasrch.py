nums = [-1, 0, 3, 5, 9, 12]
target = 9


def binarySearch(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        middle = (l + r) // 2

        if nums[middle] > target:
            r = middle - 1
        elif nums[middle] < target:
            l = middle + 1
        else:
            return middle

    return -1


print(binarySearch(nums, target))
