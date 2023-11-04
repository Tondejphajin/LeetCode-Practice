# Neet code
def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = {}  # value: index

    for index, num in enumerate(nums):
        remainding = target - num
        if remainding in hashMap:
            return [hashMap[remainding], index]
        hashMap[num] = index
    return


# My solution
def twoSum(nums, target):
    hashMap = {}
    for i in range(0, len(nums)):
        if (target - nums[i]) not in hashMap:
            hashMap[nums[i]] = i
        else:
            return [hashMap.get(target - nums[i]), i]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    output = twoSum(nums=nums, target=target)
    print(output)
