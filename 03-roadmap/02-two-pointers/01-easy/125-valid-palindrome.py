# my solution
def isPalindrome(self, s: str) -> bool:
    if s == " ":
        return True

    s_remove = ""

    for char in s:
        decimal = ord(char)

        if (
            (decimal >= 97 and decimal <= 122)
            or (decimal >= 65 and decimal <= 90)
            or (decimal >= 48 and decimal <= 57)
        ):
            s_remove += char

    left = 0
    right = len(s_remove) - 1

    while left < right:
        if s_remove[left].lower() != s_remove[right].lower():
            return False

        left += 1
        right -= 1

    return True


# neet code soln 1 (using Python features)
def isPalindrome2(s: str) -> bool:
    result = ""
    for c in s:
        if c.isalnum():
            result += c.lower()

    return result == result[::-1]


# neet code soln 2 (Two pointer algorithm)
def isPalindrome3(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not isAlphaNum(s[left]):
            left += 1

        while left < right and not isAlphaNum(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def isAlphaNum(char: str) -> bool:
    return (
        ord("A") <= ord(char) <= ord("Z")
        or ord("a") <= ord(char) <= ord("z")
        or ord("0") <= ord(char) <= ord("9")
    )


s = "A man, a plan, a canal: Panama"
print(isPalindrome3(s))
