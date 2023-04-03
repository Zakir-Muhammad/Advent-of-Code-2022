import MyQueue
file = open("day6_input.txt")
line = file.readline().strip()

def part1():
    abc = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(line)-3):
        abc_copy = abc
        abc_copy = abc_copy.replace(line[i], "")
        if line[i+1] in abc_copy:
            abc_copy = abc_copy.replace(line[i+1], "")
            if line[i+2] in abc_copy:
                abc_copy = abc_copy.replace(line[i+2], "")
                if line[i+3] in abc_copy:
                    print(i+4)


def part2():
    q = MyQueue.Queue()

    for i in range(len(line)):

        if line[i] not in q:
            q.enqueue(line[i])
            if len(q) == 14: print(i+1)

        else:
            while line[i] in q: q.dequeue()
            q.enqueue(line[i])


if __name__ == "__main__":
    #part1()
    part2()
