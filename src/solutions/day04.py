def fully_contained(task_pair: str):
	(a, b), (c, d) = get_ranges(task_pair)
	return (a <= c and b >= d) or (c <= a and d >= b)

def overlap(task_pair: str):
	(a, b), (c, d) = get_ranges(task_pair)
	return max(a, c) <= min(b, d)

def get_ranges(task_pair: str):
	s1, s2 = task_pair.split(",")
	a, b = s1.split("-")
	c, d = s2.split("-")
	a, b, c, d = int(a), int(b), int(c), int(d)
	return (a, b), (c, d)

def part1_solution(input: str):
	return sum(map(lambda _: 1, filter(fully_contained, input.split("\n"))))

def part2_solution(input: str):
	return sum(map(lambda _: 1, filter(overlap, input.split("\n"))))

test_input_string = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

tests = {
	test_input_string: (2, 4)
}