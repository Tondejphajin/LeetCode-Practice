def encode(strs):
    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    return result


def decode(strs_encode):
    result = []
    i = 0

    while i < len(strs_encode):
        j = i
        while strs_encode[j] != "#":
            j += 1
        length = int(strs_encode[i:j])
        result.append(strs_encode[j + 1 : j + 1 + length])
        i = j + 1 + length
    return result


strs = ["lint", "code", "love", "you"]
strs2 = ["we", "say", ":", "yes"]
strs_encode = encode(strs)
print(strs_encode)
print(decode(strs_encode))
