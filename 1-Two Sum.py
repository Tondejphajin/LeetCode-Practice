def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = {}  # value: index

    for index, num in enumerate(nums):
        remainding = target - num
        if remainding in hashMap:
            return [hashMap[remainding], index]
        hashMap[num] = index
    return


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    output = twoSum(nums=nums, target=target)
    print(output)
