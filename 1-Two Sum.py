def twoSum(nums: list[int], target: int) -> list[int]:
    nums.sort()
    newNums = [
        (nums[i], nums[i + 1])
        for i in range(0, len(nums) - 1)
        if nums[i] + nums[i + 1] == target
    ]
    outputList = list(newNums[0])
    return outputList


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    output = twoSum(nums=nums, target=target)
    print(output)
