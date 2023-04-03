file = open("day2_input.txt")

def part1():
    lines = file.readlines()
    move_score = {"X": 1, "Y": 2, "Z": 3}
    winning_moves = {"A": "Y", "B": "Z", "C": "X"}
    equiv_moves = {"A": "X", "B": "Y", "C": "Z"}
    score = 0


    for line in lines:
        op_move = line.strip().split(" ")[0]
        my_move = line.strip().split(" ")[1]
        score += move_score[my_move]

        if my_move == winning_moves[op_move]:
            score += 6
        elif equiv_moves[op_move] == my_move:
            score += 3

    print(score)


def part2():
    lines = file.readlines()
    moves = ["A", "B", "C"]
    result_score = {"X": 0, "Y": 3, "Z": 6}
    move_score = {"A": 1, "B": 2, "C": 3}
    winning_moves = {"A": "B", "B": "C", "C": "A"}
    score = 0

    for line in lines:
        moves1 = moves.copy()
        op_move = line.strip().split(" ")[0]
        result = line.strip().split(" ")[1]

        score += result_score[result]

        my_move_win = winning_moves[op_move]
        my_move_draw = op_move
        moves1.remove(my_move_win)
        moves1.remove(my_move_draw)
        my_move_lose = moves1[0]

        if result == "Z":
            score += move_score[my_move_win]
        elif result == "Y":
            score += move_score[my_move_draw]
        else:
            score += move_score[my_move_lose]

    print(score)

if __name__ == "__main__":
    #part1()
    part2()
