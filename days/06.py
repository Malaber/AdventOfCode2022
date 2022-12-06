import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

chars = list(lines[0].strip())
window = []

for index, char in enumerate(chars):
    window.append(char)
    if len(window) > 14:
        window.pop(0)

    if index < 3:
        continue

    if len(window) == len(list(set(window))):
        print(index + 1)
        break
