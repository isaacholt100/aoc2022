from functools import reduce
from operator import mul

def part1_solution(input: str):
	visible_trees = set()
	lines = input.split("\n")
	for i, row in enumerate(lines):
		max_height = -1
		for j, c in enumerate(row):
			height = int(c)
			if height > max_height:
				visible_trees.add((i, j))
				max_height = height
		max_height = -1
		for j in reversed(range(len(row))):
			c = row[j]
			height = int(c)
			if height > max_height:
				visible_trees.add((i, j))
				max_height = height
	for j in range(len(lines[0])):
		max_height = -1
		for i in range(len(lines)):
			height = int(lines[i][j])
			if height > max_height:
				visible_trees.add((i, j))
				max_height = height
		max_height = -1
		for i in reversed(range(len(lines))):
			height = int(lines[i][j])
			if height > max_height:
				visible_trees.add((i, j))
				max_height = height
	return len(visible_trees)

def part2_solution(input: str):
	lines = input.split("\n")
	grid_width = len(lines[0])
	grid_length = len(lines)
	# [[[up, left, down, right]]]
	view_counts = [[[None, None, None, None] for _ in range(grid_width)] for _ in range(grid_length)]
	for i in range(grid_length):
		for j in range(grid_width):
			height = lines[i][j]
			if i == 0:
				view_counts[i][j][0] = 0
			else:
				view_counts[i][j][0] = view_count(lines, i, j, 0)
			if j == 0:
				view_counts[i][j][1] = 0
			else:
				view_counts[i][j][1] = view_count(lines, i, j, 1)
	for i in reversed(range(grid_length)):
		for j in reversed(range(grid_width)):
			height = lines[i][j]
			if i == grid_length - 1:
				view_counts[i][j][2] = 0
			else:
				view_counts[i][j][2] = view_count(lines, i, j, 2)
			if j == grid_width - 1:
				view_counts[i][j][3] = 0
			else:
				view_counts[i][j][3] = view_count(lines, i, j, 3)
	max_score = 0
	for i in reversed(range(grid_length)):
		for j in reversed(range(grid_width)):
			scenic_score = reduce(mul, view_counts[i][j])
			if scenic_score > max_score:
				max_score = scenic_score
	return max_score

def view_count(lines: list[str], row: int, col: int, direction: int):
	count = 0
	if direction == 0:
		for i in reversed(range(row)):
			if lines[i][col] < lines[row][col]:
				count += 1
			else:
				count += 1
				break
	elif direction == 1:
		for j in reversed(range(col)):
			if lines[row][j] < lines[row][col]:
				count += 1
			else:
				count += 1
				break
	elif direction == 2:
		for i in range(row + 1, len(lines)):
			if lines[i][col] < lines[row][col]:
				count += 1
			else:
				count += 1
				break
	elif direction == 3:
		for j in range(col + 1, len(lines[0])):
			if lines[row][j] < lines[row][col]:
				count += 1
			else:
				count += 1
				break
	return count

test_input_string = """30373
25512
65332
33549
35390"""

tests = {
	test_input_string: (21, 8)
}