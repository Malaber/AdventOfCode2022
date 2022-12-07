import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines_input = Input.get_lines(os.path.basename(__file__))

lines = []
# line preprocessing
for line in lines_input:
    if not line == "\n":
        # remove newlines at end of the last words
        words = [word.strip() for word in line.split(" ")]
        lines.append(words)


def combine_4_spaces_into_single_column(words):
    """
    Combines 4 empty strings in list into one.

    If given the following input:
    L1'    [Q] [F] [W] [S] [V] [N] [F] [N]'
    L2' 1   2   3   4   5   6   7   8   9 '

    this results in the following words for L1:
    ["", "", "", "", "[Q]", "[F]", "[W]", "[S]", "[V]", "[N]", "[F]", "[N]"]
    Therefore we have to combine the first 4 empty strings into a single one

    :param words: List of words resulting from the current line
    :return: List of words with every 4 spaces combined into one
    """
    columns = []
    words = iter(words)
    for word in words:
        if word == "" and next(words) == "" and next(words) == "" and next(words) == "":
            columns.append("")
        else:
            columns.append(word)

    return columns


first_line_words = lines[0]
stacks_needed = len(combine_4_spaces_into_single_column(first_line_words))
# prepare as many empty stacks as we need
stacks = {}
stacks_2 = {}
for i in range(1, stacks_needed + 1):
    stacks[i] = []
    stacks_2[i] = []


def handle_move(words, stacks):
    amount = int(words[1])
    fromm = int(words[3])  # naming a variable "from" causes trouble lol
    to = int(words[5])

    for _i in range(0, amount):
        stack_to = stacks[to]
        stack_from = stacks[fromm]

        stack_to += stack_from.pop()

    return stacks


def handle_move_2(words, stacks):
    amount = int(words[1])
    fromm = int(words[3])  # naming a variable "from" causes trouble lol
    to = int(words[5])

    buffer = []
    for _i in range(0, amount):
        stack_from = stacks[fromm]

        buffer += stack_from.pop()

    buffer.reverse()
    stacks[to] += buffer

    return stacks_2


# iterate over each line
for words in lines:
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
print()
print("Part 2:")
print(answer_2)
