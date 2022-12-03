import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))


def get_priority_for_char(c: str):
    prio = ord(c)
    if prio < 91:
        prio -= 38
    else:
        prio -= 96
    return prio


priority_sum = 0
priority_sum_2 = 0

for line in lines:
    line = list(line.strip())
    length = len(line)
    half_length = int(length / 2)
    left, right = line[:half_length], line[half_length:]
    duplicate = None
    for char in left:
        if char in right:
            duplicate = char
            break
    priority = get_priority_for_char(duplicate)
    priority_sum += priority

lines = [list(s.strip()) for s in lines]
lines = iter(lines)
for line in lines:
    next_line = next(lines)
    more_next_line = next(lines)
    badge = None
    for char in line:
        if char in next_line and char in more_next_line:
            badge = char
            break
    priority = get_priority_for_char(badge)
    priority_sum_2 += priority

print("Part 1")
print(priority_sum)
print()
print("Part 2")
print(priority_sum_2)
