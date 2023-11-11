nums = [1, 2, 3, 4]


# O(n^2) solution
def ans1(nums):
    result = []
    for i in range(0, len(nums)):
        product = 1
        for j in range(0, len(nums)):
            if j == i:
                continue
            product *= nums[j]
        result.append(product)
    return result


# O(n) solution


def ans2():
    result = [1] * len(nums)

    prefix = 1

    for i in range(0, len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    print(result)

    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        result[j] *= postfix
        postfix *= nums[j]

    print(result)
