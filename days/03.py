import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

priority_sum = 0

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
    priority = ord(duplicate)
    if priority < 91:
        priority -= 38
    else:
        priority -= 96
    priority_sum += priority

print("Part 1")
print(priority_sum)
