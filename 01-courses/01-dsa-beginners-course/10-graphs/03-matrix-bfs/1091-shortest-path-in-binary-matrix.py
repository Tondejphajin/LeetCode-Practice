from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        queue.append((0, 0))
        visited.add((0, 0))

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                directions = [
                    [-1, 0],
                    [1, 0],
                    [0, -1],
                    [0, 1],
                    [-1, -1],
                    [-1, 1],
                    [1, -1],
                    [1, 1],
                ]

                for moveRow, moveCol in directions:
                    newRow, newCol = (r + moveRow, c + moveCol)
                    if (
                        min(newRow, newCol) < 0
                        or newRow == ROWS
                        or newCol == COLS
                        or (newRow, newCol) in visited
                        or grid[newRow][newCol] == 1
                    ):
                        continue

                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
            length += 1

        return -1
