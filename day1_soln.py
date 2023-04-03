file = open("day1_input.txt", "r")

def part1():
    elfs = []
    lines = file.readlines()

    sum = 0

    for line in lines:
        if (line != "\n"):
            sum += int(line.strip())
        else:
            elfs.append(sum)
            sum = 0

    print(max(elfs))


def part2():
    elfs = []
    lines = file.readlines()

    sum = 0

    for line in lines:
        if (line != "\n"):
            sum += int(line.strip())
        else:
            elfs.append(sum)
            sum = 0

    max1 = max(elfs)
    elfs.remove(max1)
    max2 = max(elfs)
    elfs.remove(max2)
    max3 = max(elfs)
    print(max1 + max2 + max3)

if __name__ == "__main__":
    #part1()
    part2()
