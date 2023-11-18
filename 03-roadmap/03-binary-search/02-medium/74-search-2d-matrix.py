def searchMatrix(matrix, target):
    rows, columns = len(matrix), len(matrix[0])

    t, b = 0, rows - 1

    while t <= b:
        row = (t + b) // 2

        if target > matrix[row][-1]:
            t += 1
        elif target < matrix[row][0]:
            b -= 1
        else:
            break

    if not (t <= b):
        return -1

    l, r = 0, columns - 1

    while l <= r:
        m = (l + r) // 2

        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 34
print(searchMatrix(matrix, target))
