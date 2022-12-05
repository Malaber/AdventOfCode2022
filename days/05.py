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


def handle_move(words, stacks):
    amount = int(words[1])
    fromm = int(words[3])  # naming a variable "from" causes trouble lol
    to = int(words[5].strip())

    for _i in range(0, amount):
        stack_to = stacks[to]
        stack_from = stacks[fromm]

        stack_to += stack_from.pop()

    return stacks


def handle_move_2(words, stacks):
    amount = int(words[1])
    fromm = int(words[3])  # naming a variable "from" causes trouble lol
    to = int(words[5].strip())

    buffer = []
    for _i in range(0, amount):
        stack_from = stacks[fromm]

        buffer += stack_from.pop()

    buffer.reverse()
    stacks[to] += buffer

    return stacks_2


for line in lines:
    words = line.split(" ")
    print()
    match words[0]:
        case "1":
            continue
        case "move":
            # handle moves
            stacks = handle_move(words, stacks)
            stacks_2 = handle_move_2(words, stacks_2)
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
