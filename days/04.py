import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))


def get_bounds(range):
    return [int(i) for i in range.split("-")]


fully_contained_counter = 0
overlap_at_all_counter = len(lines)
for line in lines:
    first, second = line.strip().split(",")
    first_low, first_high = get_bounds(first)
    second_low, second_high = get_bounds(second)

    if second_low >= first_low and second_high <= first_high or first_low >= second_low and first_high <= second_high:
        fully_contained_counter += 1

    if first_low <= second_low and first_high < second_low or second_low <= first_low and second_high < first_low:
        overlap_at_all_counter -= 1

print("Part 1:")
print(fully_contained_counter)
print()
print("Part 2:")
print(overlap_at_all_counter)
