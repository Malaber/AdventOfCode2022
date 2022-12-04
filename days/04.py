import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))


def get_bounds(range):
    return [int(i) for i in range.split("-")]


counter = 0
for line in lines:
    first, second = line.strip().split(",")
    first_low, first_high = get_bounds(first)
    second_low, second_high = get_bounds(second)

    fully_contained = False
    if second_low >= first_low and second_high <= first_high:
        fully_contained = True
    elif first_low >= second_low and first_high <= second_high:
        fully_contained = True

    if fully_contained:
        counter += 1

print("Part 1")
print(counter)
