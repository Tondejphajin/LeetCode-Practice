def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    maxL = 0
    charSet = set()
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        maxL = max(maxL, r - l + 1)
    return maxL


s = "pwwkew"
print(lengthOfLongestSubstring(s))
