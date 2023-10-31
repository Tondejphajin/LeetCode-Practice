# brute force

# sorting


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
