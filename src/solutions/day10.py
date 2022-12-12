def part1_solution(input: str):
	sum_strengths = 0
	cycle = 0
	x = 1
	for line in input.split("\n"):
		if cycle % 40 == 19:
			signal_strength = x * (cycle + 1)
			sum_strengths += signal_strength
		if line == "noop":
			cycle += 1
		else:
			cycle += 2
			if cycle % 40 == 20:
				signal_strength = x * cycle
				sum_strengths += signal_strength
			v = int(line.split(" ")[1])
			x += v
	return sum_strengths

def change_at_index(s: str, index: int, char: str):
	return s[:index] + char + s[index + 1:]

def part2_solution(input: str):
	image_matrix = [["." for _ in range(40)] for _ in range(6)]
	image = (("." * 40) + "\n") * 6
	cycle = 0
	x = 1
	for line in input.split("\n"):
		if line == "noop":
			col = cycle % 40
			cycle += 1
			if col in [x - 1, x, x + 1]:
				row = cycle // 40
				image_matrix[row][col] = "#"
		else:
			col1 = cycle % 40
			cycle += 1
			col2 = cycle % 40
			if col1 in [x - 1, x, x + 1]:
				row1 = (cycle - 1) // 40
				image_matrix[row1][col1] = "#"
			if col2 in [x - 1, x, x + 1]:
				row2 = cycle // 40
				image_matrix[row2][col2] = "#"
			cycle += 1
			v = int(line.split(" ")[1])
			x += v
	return "\n" + ("\n".join(["".join(row) for row in image_matrix]))

test_input_string = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

part_2_test_answer = """\n##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

tests = {
	test_input_string: (13140, part_2_test_answer)
}