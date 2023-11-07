from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    hashMap = defaultdict(list)

    for str in strs:
        alphabets = [0] * 26
        for s in str:
            index = ord(s) - ord("a")
            if index >= 0:
                alphabets[index] += 1
        hashMap[tuple(alphabets)].append(str)

    return hashMap.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
