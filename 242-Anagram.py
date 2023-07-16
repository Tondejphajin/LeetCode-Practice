s = "anagram"
t = "nagaram"


def isAnagram(s: str, t: str):
    s_dict = {}
    t_dict = {}
    for letter in s:
        try:
            if s_dict[letter] == letter:
                s_dict[letter] += 1
        except Exception as e:
            pass
        s_dict[letter] = 0

    for letter in t:
        try:
            if t_dict[letter] == letter:
                t_dict[letter] += 1
        except Exception as e:
            pass
        t_dict[letter] = 0

    return s_dict, t_dict


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    s_result, t_result = isAnagram(s, t)
    print(s_result)
    print(t_result)
