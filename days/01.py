import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

elves = {}
elve_counter = 0
for line in lines:
    line = line.strip()
    if line == "":
        elve_counter += 1
        continue

    calories = int(line)
    if elves.get(elve_counter):
        elves[elve_counter] += calories
    else:
        elves[elve_counter] = calories

print(max(elves.values()))
