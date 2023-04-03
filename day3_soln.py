#a to z ord(c)-96
#A to Z ord(c)-38

file = open("day3_input.txt")
lines = file.readlines()
lower = "abcdefghijklmnopqrstuvwxyz"
#upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1():
    priority = 0

    for line in lines:
        line = line.strip()
        mid = len(line)//2
        first = line[:mid]
        last = line[mid:]

        for c in first:
            if c in last:
                if c in lower: priority += ord(c)-96
                else: priority += ord(c)-38
                break

    print(priority)

def part2():
    priority = 0

    for i in range(0, len(lines), 3):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()

        for c in line1:
            if c in line2 and c in line3:
                if c in lower: priority += ord(c)-96
                else: priority += ord(c)-38
                break

    print(priority)

if __name__ == "__main__":
    part1()
    part2()
