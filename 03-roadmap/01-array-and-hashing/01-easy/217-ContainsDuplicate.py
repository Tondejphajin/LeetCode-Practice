# Dict (my solution)
def containsDuplicate(self, nums: list[int]) -> bool:
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
            return True
    return False


# HashSet
def containDuplicate(nums: list[int]) -> bool:
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False


# top 0.01
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
