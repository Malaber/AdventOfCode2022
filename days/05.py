import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

lines.remove("\n")


def combine_4_spaces_into_single_column(words):
    columns = []
    words = iter(words)
    for word in words:
        if word == "" and next(words) == "" and next(words) == "" and next(words).strip() == "":
            columns.append("")
        else:
            columns.append(word.strip())

    return columns


built_stacks = False
stacks = {}
stacks_2 = {}
for i in range(1, 10):
    stacks[i] = []
    stacks_2[i] = []


def handle_move(words, stacks, stacks_2):
    amount = int(words[1])
    fromm = int(words[3])  # naming a variable "from" causes trouble lol
    to = int(words[5].strip())

    buffer_2 = []
    for _i in range(0, amount):
        stacks[to] += stacks[fromm].pop()

        stack_from_2 = stacks_2[fromm]
        buffer_2.insert(0, stack_from_2.pop())

    stacks_2[to] += buffer_2

    return stacks, stacks_2


for line in lines:
    words = line.split(" ")
    print()
    match words[0]:
        case "1":
            continue
        case "move":
            # handle moves
            stacks, stacks_2 = handle_move(words, stacks, stacks_2)
        case _:
            columns = combine_4_spaces_into_single_column(words)
            for i, cell in enumerate(columns):
                if cell == "":
                    continue
                else:
                    stacks[i + 1].insert(0, (cell[1]))
                    stacks_2[i + 1].insert(0, (cell[1]))

answer = "".join([stack.pop() for stack in stacks.values()])
answer_2 = "".join([stack.pop() for stack in stacks_2.values()])
print("Part 1:")
print(answer)
print("Part 2:")
print(answer_2)
