def part1(lines: list[str]) -> int:
    cycle = 1
    x = 1
    sum = 0
    cycles = [20, 60, 100, 140, 180, 220]

    for line in lines:
        if "noop" in line:
            sum = add_cycle(cycle, cycles, x, sum)
            cycle += 1

        elif "addx" in line:
            v = int(line.replace("addx ", "").strip())
            sum = add_cycle(cycle, cycles, x, sum)
            cycle += 1
            sum = add_cycle(cycle, cycles, x, sum)
            cycle += 1
            x += v

    return sum


def add_cycle(cycle: int, cycles: list[int], x: int, sum: int) -> int:
    if cycle in cycles: return sum + x*cycle
    else: return sum


def part2(lines: str):
    cycle = 1
    x = 1
    row = ""

    for line in lines:
        if "noop" in line:
            # During the cycle
            row = draw((cycle-1)%40, x, row)
            cycle += 1

        elif "addx" in line:
            v = int(line.replace("addx ", "").strip())
            # During the first cycle
            row = draw((cycle-1)%40, x, row)
            cycle += 1
            # During the second cycle
            row = draw((cycle-1)%40, x, row)
            cycle += 1
            x += v

    print(row[:40])
    print(row[40:80])
    print(row[80:120])
    print(row[120:160])
    print(row[160:200])
    print(row[200:])

def draw(pixel_pos: int, sprite_mid: int, row: str) -> str:
    if pixel_pos == sprite_mid-1 or pixel_pos == sprite_mid or pixel_pos == sprite_mid+1:
        return row + "#"
    else: return row + "."


if __name__ == "__main__":
    file = open("day10_input.txt", "r")
    #file = open("text_input.txt", "r")
    lines = file.readlines()
    #print(part1(lines))
    part2(lines)
