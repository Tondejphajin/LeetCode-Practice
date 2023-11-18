# my solution


def twoSum(nums, target) -> list[int]:
    left = 0
    right = len(nums) - 1
    result = []
    while left < right:
        if nums[left] + nums[right] == target:
            left += 1
            right += 1
            result.append(left)
            result.append(right)
            break

        if nums[left] + nums[right] > target:
            right -= 1
            continue

        if nums[left] + nums[right] < target:
            left += 1
            continue

    return result


# neetcode


def twoSum2(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            left += 1


numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))
