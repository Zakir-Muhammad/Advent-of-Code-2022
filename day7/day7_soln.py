from MyDir import *
from MyFile import *

file = open("day7_input.txt")
#file = open("test_input.txt")
lines = file.readlines()


# Solves part1
def part1():
    root = build_tree()
    acceptable = []
    add_allowed_dirs(root, acceptable)

    size_sum = 0
    for dir in acceptable: size_sum += dir.get_size()
    print(size_sum)


# Adds all directories with size <= 100,000 to the supplied list
def add_allowed_dirs(dir: Directory, acceptable: list[Directory]) -> None:
    if dir is None: return
    if dir.get_size() <= 100000: acceptable.append(dir)
    for child in dir.sub:
        if isinstance(child, Directory): add_allowed_dirs(child, acceptable)


# Same as above, but for part2
def add_allowed_dirs2(dir: Directory, acceptable: list[Directory], threshold: int) -> None:
    if dir is None: return
    if dir.get_size() >= threshold: acceptable.append(dir)
    for child in dir.sub:
        if isinstance(child, Directory): add_allowed_dirs2(child, acceptable, threshold)


# Builds the directory tree and returns the root
def build_tree() -> Directory:
    root = Directory(None, "/")
    curr = root

    for line in lines:

        # If it's a command
        if line.find("$") == 0:
            line = line.strip("$ \n")

            # Do nothing if ls
            # Behaviour for cd
            if line.find("cd") == 0:
                name = line.split(" ")[1]
                if name == "..": curr = curr.parent # Move upwards
                elif name == "/": curr = root # Move into the root directory
                else:
                    if not name in curr:
                        curr.add_child(Directory(curr, name))
                    curr = curr.change(name)


        # If it's a listing of a dir
        else:
            line = line.strip()

            # If it's a folder
            if line.find("dir") == 0:
                name = line.replace("dir ", "")
                if not name in curr: curr.add_child(Directory(curr, name))

            # If it's a file
            else:
                size = int(line.split(" ")[0])
                name = line.split(" ")[1]
                if not name in curr: curr.add_child(File(curr, name, size))

    return root


# Solves part2
def part2():
    root = build_tree()
    used_space = root.get_size()
    remaining_space = 70000000 - used_space
    additional_space_needed = 30000000 - remaining_space

    acceptable = []
    add_allowed_dirs2(root, acceptable, additional_space_needed)

    min = acceptable[0].get_size()
    for i in range(1, len(acceptable)):
        size = acceptable[i].get_size()
        if size < min: min = size

    print(min)


if __name__ == "__main__":
    # part1()
    part2()
