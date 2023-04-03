from __future__ import annotations
import doctest


def part1(lines: list[str]) -> int:
    """
    >>> lines = ["30373\\n", "25512\\n", "65332\\n", "33549\\n", "35390\\n"]
    >>> part1(lines)
    21
    """

    grid = to_list(lines)
    count = len(grid)*2 + (len(grid[0])-2)*2

    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):

            up = check_direction(grid, row, col, 0, row, False)
            down = check_direction(grid, row, col, row+1, len(grid), False)
            right = check_direction(grid, row, col, col+1, len(grid[row]), True)
            left = check_direction(grid, row, col, 0, col, True)
            if any([up, down, right, left]) == True: count += 1

    return count


def part2(lines: list[str]) -> int:
    """
    >>> lines = ["30373\\n", "25512\\n", "65332\\n", "33549\\n", "35390\\n"]
    >>> part2(lines)
    8
    """
    grid = to_list(lines)
    scores = []

    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            up = count_view(grid, row, col, row-1, -1, False, -1)
            down = count_view(grid, row, col, row+1, len(grid), False, 1)
            right = count_view(grid, row, col, col+1, len(grid[row]), True, 1)
            left = count_view(grid, row, col, col-1, -1, True, -1)
            scores.append(up*down*left*right)

    return max(scores)


def count_view(grid: list[list[int]], row_index: int, col_index: int, start: int, end: int, horizontal: bool, direction: int) -> int:
    count = 0

    if horizontal:
        for col in range(start, end, direction):
            count += 1
            if grid[row_index][col] >= grid[row_index][col_index]: return count

    else:
        for row in range(start, end, direction):
            count += 1
            if grid[row][col_index] >= grid[row_index][col_index]: return count

    return count


def check_direction(grid: list[list[int]], row_index: int, col_index: int, start: int, end: int, horizontal: bool) -> bool:
    """
    Returns whether the tree at grid[row_index][col_index] is visible or not

    >>> grid = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]
    >>> check_direction(grid, 1, 1, 1, 5, True)
    False
    >>> check_direction(grid, 2, 2, 0, 2, False)
    False
    >>> check_direction(grid, 3, 2, 0, 2, True)
    True
    """

    if horizontal:
        for col in range(start, end):
            if grid[row_index][col] >= grid[row_index][col_index]: return False
        return True

    else:
        for row in range(start, end):
            if grid[row][col_index] >= grid[row_index][col_index]: return False
        return True


def to_list(lines: str) -> list[list[int]]:
    """
    Converts the string representation of the map to a 2d list which it returns

    >>> lines = ["30373\\n", "25512\\n", "65332\\n", "33549\\n", "35390\\n"]
    >>> to_list(lines)
    [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]
    """

    l = []

    for line in lines:
        s = list(line.strip())
        l.append([int(i) for i in s])

    return l


def remove_edges(l: list[list[int]]) -> int:
    """
    Removes the edges of the grid and returns how many edges there were

    >>> l = to_list(["30373\\n", "25512\\n", "65332\\n", "33549\\n", "35390\\n"])
    >>> remove_edges(l)
    16
    >>> l
    [[5, 5, 1], [5, 3, 3], [3, 5, 4]]
    """

    count = len(l)*2 + (len(l[0])-2)*2

    l.pop(0)
    l.pop(-1)
    for row in l:
        row.pop(0)
        row.pop(-1)

    return count


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    file = open("day8_input.txt", "r")
    lines = file.readlines()

    #print(part1(lines))
    print(part2(lines))
