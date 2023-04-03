def part1(lines: str):
    hr = hc = 0
    tr = tc = 0
    visited = {(0,0)}

    for line in lines:
        repeats = int(line.strip().split(" ")[1])
        direction = line.split(" ")[0]

        for _ in range(repeats):
            hpos = move(hr, hc, direction)
            hr = hpos[0]
            hc = hpos[1]

            if not touching(hr, hc, tr, tc):
                # Need to move diagonally
                if hr != tr and hc != tc:
                    tpos = diag_move(hr, hc, tr, tc)

                # Move regularly
                else:
                    tpos = adj_move(hr, hc, tr, tc)

                tr = tpos[0]
                tc = tpos[1]
                visited.add(tpos)
    return len(visited)


def adj_move(hrow: int, hcol: int, trow: int, tcol: int) -> tuple[int, int]:
    """
    Returns the position adjacent to tail that is also adjacent to head
    """
    if touching(hrow, hcol, trow+1, tcol): return (trow+1, tcol)
    if touching(hrow, hcol, trow-1, tcol): return (trow-1, tcol)
    if touching(hrow, hcol, trow, tcol+1): return (trow, tcol+1)
    if touching(hrow, hcol, trow, tcol-1): return (trow, tcol-1)


def diag_move(hrow: int, hcol: int, trow: int, tcol: int) -> tuple[int, int]:
    """
    Returns the position diagonal to tail that is also adjacent
    """
    if touching(hrow, hcol, trow+1, tcol+1): return (trow+1, tcol+1)
    if touching(hrow, hcol, trow-1, tcol-1): return (trow-1, tcol-1)
    if touching(hrow, hcol, trow+1, tcol-1): return (trow+1, tcol-1)
    if touching(hrow, hcol, trow-1, tcol+1): return (trow-1, tcol+1)


def move(row: int, col: int, direction: str) -> tuple[int, int]:
    """
    Returns the position of head once it has moved.
    """
    match direction:
        case "U": return (row - 1, col)
        case "D": return (row + 1, col)
        case "L": return (row, col - 1)
        case "R": return (row, col + 1)


def touching(hrow: int, hcol: int, trow: int, tcol: int) -> bool:
    """
    Returns whether or not (trow, tcol) is adjacent or on to (hrow, hcol)
    """
    rdif = hrow - trow
    cdif = hcol - tcol

    # On top
    if rdif == cdif == 0: return True
    # Adjacent
    if abs(rdif) + abs(cdif) == 1: return True
    #Diagonal
    if abs(rdif) == abs(cdif) == 1: return True
    return False


def part2(lines: str):
    knots = [(0,0) for _ in range(10)]
    visited = {(0,0)}

    for line in lines:
        repeats = int(line.strip().split(" ")[1])
        direction = line.split(" ")[0]

        for _ in range(repeats):
            hpos = knots[0]
            knots[0] = move(hpos[0], hpos[1], direction)

            for i in range(1, len(knots)):
                hpos = knots[i-1]
                hr = hpos[0]
                hc = hpos[1]

                tpos = knots[i]
                tr = tpos[0]
                tc = tpos[1]

                if not touching(hr, hc, tr, tc):
                    # Need to move diagonally
                    if hr != tr and hc != tc:
                        knots[i] = diag_move(hr, hc, tr, tc)

                    # Move regularly
                    else:
                        knots[i] = adj_move(hr, hc, tr, tc)

                if i == 9: visited.add(knots[i])
    return len(visited)


if __name__ == "__main__":
    file = open("day9_input.txt", "r")
    lines = file.readlines()
    # lines = ["R 4\n",
    #         "U 4\n",
    #         "L 3\n",
    #         "D 1\n",
    #         "R 4\n",
    #         "D 1\n",
    #         "L 5\n",
    #         "R 2\n"]
    # lines = ["R 5\n",
    #          "U 8\n",
    #          "L 8\n",
    #          "D 3\n",
    #          "R 17\n",
    #          "D 10\n",
    #          "L 25\n",
    #          "U 20\n"]
    #print(part1(lines))
    print(part2(lines))
