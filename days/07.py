import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

# 🔥
lines = Input.get_lines(os.path.basename(__file__))

dirs = {
    "/": {}
}
current_dir = []

for line in lines:
    words = [word.strip() for word in line.split(" ")]
    if words[0] == "$":
        # input
        if words[1] == "cd":
            match words[2]:
                case "/":
                    current_dir = ["/"]
                case "..":
                    current_dir.pop()
                case _:
                    current_dir.append(words[2])

        else:
            # ignore ls
            pass
    else:
        # output
        if words[1] == "dir":
            pass
        else:
            size = int(words[1])
            name = words[2]


    print(current_dir)

print()
