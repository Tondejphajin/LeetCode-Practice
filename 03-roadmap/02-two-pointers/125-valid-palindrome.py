def removeNonChar(s: str) -> str:
    result = ""
    for char in s.lower():
        unicodeNum = ord(char)
        if unicodeNum >= 97 and unicodeNum <= 122:
            result += char
    return result


def isPalindrome(s: str) -> bool:
    s_char_only = removeNonChar(s)
    if s_char_only == "":
        return True
    return s_char_only == s_char_only[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
