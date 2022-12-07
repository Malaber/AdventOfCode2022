import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines_input = Input.get_lines(os.path.basename(__file__))

lines = []
# line preprocessing
for line in lines_input:
    # filter out unnecessary lines
    if not line == "\n" or line.startswith(" 1"):
        # remove newlines at end of the last words
        words = [word.strip() for word in line.split(" ")]
        lines.append(words)


def combine_4_spaces_into_single_column(words):
    """
    Combines 4 empty strings in list into one.

    If given the following input:
    L1'    [Q] [F]'
    L2' 1   2   3 '

    this results in the following words for L1:
    ["", "", "", "", "[Q]", "[F]"]
    Therefore we have to combine the first 4 empty strings into a single one.

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


stacks_needed = len(combine_4_spaces_into_single_column(lines[0]))
# prepare as many empty stacks as we need
# stacks for the crane 9000
stacks = {}
# stacks for the crane 9001
stacks_2 = {}
for i in range(1, stacks_needed + 1):
    stacks[i] = []
    stacks_2[i] = []


def handle_move(words, stacks):
    # handle move for crane 9000
    amount = int(words[1])
    fromm = int(words[3])  # naming a variable "from" causes trouble lol
    to = int(words[5])

    for _i in range(0, amount):
        stack_to = stacks[to]
        stack_from = stacks[fromm]

        stack_to += stack_from.pop()

    return stacks


def handle_move_2(words, stacks):
    # handle move for crane 9001
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
    if words[0] == "move":
        # handle moves
        stacks = handle_move(words, stacks)
        stacks_2 = handle_move_2(words, stacks_2)
    else:
        # build up stacks from top to bottom
        columns = combine_4_spaces_into_single_column(words)
        for i, cell in enumerate(columns):
            if cell == "":
                # ignore empty cells
                continue
            else:
                # push current container at bottom of stack
                stacks[i + 1].insert(0, (cell[1]))
                stacks_2[i + 1].insert(0, (cell[1]))

answer = "".join([stack.pop() for stack in stacks.values()])
answer_2 = "".join([stack.pop() for stack in stacks_2.values()])
print("Part 1:")
print(answer)
print()
print("Part 2:")
print(answer_2)
