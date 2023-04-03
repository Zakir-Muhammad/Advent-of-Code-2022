import MyStack
import re
file = open("day5_input.txt", "r")
lines = file.readlines()


def part1():

    for line in lines:
        line = line.strip()
        #print(line)
        repeat = int(re.findall("move ([0-9]{1,2})", line)[0])
        #repeat = int(line[5])
        start = int(re.findall("from ([1-9])", line)[0])-1
        #start = int(line[12])-1
        end = int(re.findall("to ([1-9])", line)[0])-1
        #end = int(line[17])-1

        for _ in range(repeat):
            move = stacks[start].pop()
            stacks[end].push(move)

    tops = ""
    for stack in stacks:
        tops += stack.pop()

    print(tops)


def part2():

    for line in lines:
        line = line.strip()
        #print(line)
        repeat = int(re.findall("move ([0-9]{1,2})", line)[0])
        #repeat = int(line[5])
        start = int(re.findall("from ([1-9])", line)[0])-1
        #start = int(line[12])-1
        end = int(re.findall("to ([1-9])", line)[0])-1
        #end = int(line[17])-1

        temp_string = ""
        for _ in range(repeat):
            temp_string += stacks[start].pop()

        temp_stack = MyStack.Stack(temp_string)
        while not temp_stack.empty():
            stacks[end].push(temp_stack.pop())

    tops = ""
    for stack in stacks:
        tops += stack.pop()

    print(tops)



if __name__ == "__main__":
    strings = [
    'mjcbfrlh',
    'zcd',
    'hjfcngw',
    'pjdmtsb',
    'ncdrj',
    'wldqpjgz',
    'pztfrh',
    'lvmg',
    'cbgpfqrj']

    stacks = []
    for string in strings: stacks.append(MyStack.Stack(string))

    #part1()
    part2()
