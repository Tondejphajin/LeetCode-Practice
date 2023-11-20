def maxArea(height):
    max_area = 0
    for i in range(0, len(height)):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area


def maxArea2(height):
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea2(height))
