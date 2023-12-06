def numOfSubarrays(arr, k, threshold):
    l, r = 0, 0
    result, curSum = 0, 0
    while r < len(arr):
        curSum += arr[r]
        if (r - l + 1) % k == 0:
            if curSum / k >= threshold:
                result += 1
            curSum -= arr[l]
            l += 1
        r += 1

    return result


arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
print(numOfSubarrays(arr, k, threshold))
