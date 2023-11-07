# solution
from collections import defaultdict


def topKfrequent(nums, k):
    hashMap = defaultdict(int)
    for num in nums:
        hashMap[num] += 1

    print(hashMap)

    freq = [[] for i in range(0, len(nums) + 1)]

    print(freq)

    for key, value in hashMap.items():
        freq[value].append(key)

    print(freq)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for element in freq[i]:
            result.append(element)
            if len(result) == k:
                return result


print(topKfrequent([1, 1, 1, 2, 2, 3], 2))
