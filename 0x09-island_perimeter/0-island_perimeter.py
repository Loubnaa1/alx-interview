#!/usr/bin/python3
"""funtion island perimeter.
"""


def island_perimeter(grid):
    """
    Function that calculate the perimeter of the island in the grid.
    """
    flag = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    flag += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    flag += 1
                if j == 0 or grid[i][j - 1] == 0:
                    flag += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    flag += 1
    return flag
