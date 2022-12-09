import math

def pos_dist(pos1: list[int], pos2: list[int]):
	return ((pos1[0] - pos2[0]), (pos1[1] - pos2[1]))

def get_move_dist(dist: int):
	if dist == -2 or dist == 2:
		return dist // 2
	if dist == 1:
		return 1
	if dist == -1:
		return -1
	return 0

def part1_solution(input: str):
	return get_visited_positions(input, 2)

def get_visited_positions(input: str, knots: int):
	rope_position = [[0, 0] for _ in range(knots)]
	visited_positions = set()
	for line in input.split("\n"):
		direction, distance = line.split(" ")
		distance = int(distance)
		for _ in range(distance):
			if direction == "U":
				rope_position[0][1] += 1
			elif direction == "R":
				rope_position[0][0] += 1
			elif direction == "D":
				rope_position[0][1] -= 1
			elif direction == "L":
				rope_position[0][0] -= 1
			for i in range(knots - 1):
				knot_position = rope_position[i]
				next_knot_position = rope_position[i + 1]
				dist = pos_dist(knot_position, next_knot_position)
				if abs(dist[0]) > 1 or abs(dist[1]) > 1:
					move_vec = [get_move_dist(dist[0]), get_move_dist(dist[1])]
					next_knot_position[0] += move_vec[0]
					next_knot_position[1] += move_vec[1]
			visited_positions.add((rope_position[-1][0], rope_position[-1][1]))
	return len(visited_positions)

def part2_solution(input: str):
	return get_visited_positions(input, 10)

test_input_string_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input_string_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

tests = {
	test_input_string_1: (13, 1),
	test_input_string_2: (None, 36)
}