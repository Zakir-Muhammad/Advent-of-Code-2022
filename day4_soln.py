file = open("day4_input.txt", "r")
lines = file.readlines()

def part1():
    count = 0

    for line in lines:
        line = line.strip()
        range1 = line.split(",")[0]
        b1 = int(range1.split("-")[0])
        e1 = int(range1.split("-")[1])
        range2 = line.split(",")[1]
        b2 = int(range2.split("-")[0])
        e2 = int(range2.split("-")[1])

        if (b1 <= b2 and e1 >= e2) or (b2 <= b1 and e2 >= e1): count += 1

    print(count)


def part2():
    count = 0

    for line in lines:
        line = line.strip()
        range1 = line.split(",")[0]
        b1 = int(range1.split("-")[0])
        e1 = int(range1.split("-")[1])
        range2 = line.split(",")[1]
        b2 = int(range2.split("-")[0])
        e2 = int(range2.split("-")[1])

        if (b1 <= b2 <= e1) or (b2 <= b1 <= e2): count += 1

    print(count)


if __name__ == "__main__":
    part1()
    part2()
