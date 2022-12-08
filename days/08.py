import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))


def is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, direction):
    if i == 0 or j == 0 or i == grid_max_i or j == grid_max_j:
        return True

    match direction:
        case "up":
            height = tree_grid[i][j]
            while i > 0:
                next_height = tree_grid[i-1][j]
                if next_height >= height:
                    return False
                i -= 1
            
        case "down":
            height = tree_grid[i][j]
            while i < grid_max_i:
                next_height = tree_grid[i+1][j]
                if next_height >= height:
                    return False
                i += 1

        case "left":
            height = tree_grid[i][j]
            while j > 0:
                next_height = tree_grid[i][j-1]
                if next_height >= height:
                    return False
                j -= 1

        case "right":
            height = tree_grid[i][j]
            while j < grid_max_j:
                next_height = tree_grid[i][j+1]
                if next_height >= height:
                    return False
                j += 1
        
    return True


def get_tree_viewing_distance(i, j, grid_max_i, grid_max_j, tree_grid, direction, height=None):
    if height is None:
        height = tree_grid[i][j]
    match direction:
        case "up":
            if i == 0:
                return 0

            next_tree = tree_grid[i-1][j]
            if next_tree >= height:
                return 1
            else:
                return 1 + get_tree_viewing_distance(i-1, j, grid_max_i, grid_max_j, tree_grid, direction, height=height)

        case "down":
            if i == grid_max_i:
                return 0

            next_tree = tree_grid[i+1][j]
            if next_tree >= height:
                return 1
            else:
                return 1 + get_tree_viewing_distance(i+1, j, grid_max_i, grid_max_j, tree_grid, direction, height=height)

        case "left":
            if j == 0:
                return 0

            next_tree = tree_grid[i][j-1]
            if next_tree >= height:
                return 1
            else:
                return 1 + get_tree_viewing_distance(i, j-1, grid_max_i, grid_max_j, tree_grid, direction, height=height)

        case "right":
            if j == grid_max_j:
                return 0

            next_tree = tree_grid[i][j+1]
            if next_tree >= height:
                return 1
            else:
                return 1 + get_tree_viewing_distance(i, j+1, grid_max_i, grid_max_j, tree_grid, direction, height=height)


def get_tree_scenic_score(i, j, grid_max_i, grid_max_j, tree_grid):
    return get_tree_viewing_distance(i, j, grid_max_i, grid_max_j, tree_grid, "up") * get_tree_viewing_distance(i, j, grid_max_i, grid_max_j, tree_grid, "down") * get_tree_viewing_distance(i, j, grid_max_i, grid_max_j, tree_grid, "left") * get_tree_viewing_distance(i, j, grid_max_i, grid_max_j, tree_grid, "right")


tree_grid = []
for i, line in enumerate(lines):
    trees = list(line.strip())
    tree_grid.append(trees)

visible_sum = 0
grid_max_i = len(tree_grid) - 1
grid_max_j = len(tree_grid[0]) - 1
for i, line in enumerate(tree_grid):
    for j, tree in enumerate(line):
        if is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "up") or is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "down") or is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "left") or is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "right"):
            visible_sum += 1

max_scenic_score = 0
for i, line in enumerate(tree_grid):
    for j, tree in enumerate(line):
        score = get_tree_scenic_score(i, j, grid_max_i, grid_max_j, tree_grid)
        if score > max_scenic_score:
            max_scenic_score = score

print("Part 1:")
print(visible_sum)
print()
print("Part 2:")
print(max_scenic_score)
