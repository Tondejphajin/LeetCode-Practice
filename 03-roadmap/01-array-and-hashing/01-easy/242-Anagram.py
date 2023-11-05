from collections import Counter


def isAnagram_1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(0, len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

    for key in s_dict:
        if s_dict[key] != t_dict.get(key, 0):
            return False

    return True


def isAnagram_2(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def isAnagram_3(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram_1(s, t))
    print(isAnagram_2(s, t))
    print(isAnagram_3(s, t))
