import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

datastream = list(lines[0].strip())


def find_starting_index(chars, consecutive_changing_chars):
    window = []
    for index, char in enumerate(chars):
        window.append(char)
        if len(window) > consecutive_changing_chars:
            window.pop(0)

        if not index > consecutive_changing_chars:
            continue

        if len(window) == len(set(window)):
            return index + 1


print("Part 1:")
print(find_starting_index(datastream, 4))
print()
print("Part 2:")
print(find_starting_index(datastream, 14))
