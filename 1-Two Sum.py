def twoSum(nums: list[int], target: int) -> list[int]:
    for num in nums:
        remainding = target - num
        if remainding in nums:
            return [num, remainding]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    output = twoSum(nums=nums, target=target)
    print(output)
