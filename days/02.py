import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSOR_POINTS = 3

LOOSE_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6


def convert_to_name_and_points(char):
    match char:
        case "X" | "A":
            return "rock", ROCK_POINTS
        case "Y" | "B":
            return "paper", PAPER_POINTS
        case "Z" | "C":
            return "scissors", SCISSOR_POINTS


def convert_to_round_points_2(you, elf):
    match you:
        case "X":
            # need to loose
            match elf:
                case "rock":
                    return SCISSOR_POINTS + LOOSE_POINTS
                case "paper":
                    return ROCK_POINTS + LOOSE_POINTS
                case "scissors":
                    return PAPER_POINTS + LOOSE_POINTS
        case "Y":
            # need to draw
            match elf:
                case "rock":
                    return ROCK_POINTS + DRAW_POINTS
                case "paper":
                    return PAPER_POINTS + DRAW_POINTS
                case "scissors":
                    return SCISSOR_POINTS + DRAW_POINTS
        case "Z":
            # need to win
            match elf:
                case "rock":
                    return PAPER_POINTS + WIN_POINTS
                case "paper":
                    return SCISSOR_POINTS + WIN_POINTS
                case "scissors":
                    return ROCK_POINTS + WIN_POINTS

    raise Exception(f"{you}, e: {elf}")


def get_you_round_points(you, elf):
    if you == elf:
        return DRAW_POINTS
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

    return WIN_POINTS if won else LOOSE_POINTS


score_1 = 0
score_2 = 0

for line in lines:
    elf, you = line.strip().split(' ')

    elf, elf_points = convert_to_name_and_points(elf)
    you_name, you_points = convert_to_name_and_points(you)

    you_round_points = get_you_round_points(you_name, elf)

    score_1 += you_round_points + you_points

    score_2 += convert_to_round_points_2(you, elf)

print("Part 1")
print(score_1)
print()
print("Part 2")
print(score_2)
