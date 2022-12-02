import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))


def convert_to_name_and_points(char):
    match char:
        case "X" | "A":
            return "rock", 1
        case "Y" | "B":
            return "paper", 2
        case "Z" | "C":
            return "scissors", 3


def get_you_round_points(you, elf):
    if you == elf:
        return 3
    won = False
    match you:
        case "rock":
            if elf == "scissors":
                won = True
        case "paper":
            if elf == "rock":
                won = True
        case "scissors":
            if elf == "paper":
                won = True

    return 6 if won else 0


score = 0

for line in lines:
    elf, you = line.strip().split(' ')

    elf, elf_points = convert_to_name_and_points(elf)
    you, you_points = convert_to_name_and_points(you)

    you_round_points = get_you_round_points(you, elf)

    score += you_round_points + you_points

print("Part 1")
print(score)
