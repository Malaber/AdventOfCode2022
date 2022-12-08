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


tree_grid = []
for i, line in enumerate(lines):
    trees = list(line.strip())
    tree_grid.append(trees)

print(tree_grid)
visible_sum = 0
grid_max_i = len(tree_grid) - 1
grid_max_j = len(tree_grid[0]) - 1
for i, line in enumerate(tree_grid):
    for j, tree in enumerate(line):
        if is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "up") or is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "down") or is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "left") or is_tree_visible(i, j, grid_max_i, grid_max_j, tree_grid, "right"):
            visible_sum += 1

print(visible_sum)

