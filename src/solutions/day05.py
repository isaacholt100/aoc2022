def get_crate_stacks(input: str):
	lines = input.split("\n")
	crate_stacks: list[list[str]] = [[] for i in range(len(lines[0]) // 4 + 1)] # first item in each sub list is top of stack
	i = 0
	while not lines[i].startswith(" 1 "):
		line = lines[i]
		for j in range(len(line) // 4 + 1):
			char = line[j * 4 + 1]
			if char.isalpha():
				crate_stacks[j].append(char)
		i += 1
	i += 1
	for stack in crate_stacks:
		stack.reverse()
	assert lines[i] == ""
	i += 1
	return crate_stacks, lines[i:]

def part1_solution(input: str):
	crate_stacks, rest_of_lines = get_crate_stacks(input)
	for line in rest_of_lines:
		s1, s2 = line.split("from ")
		count = int(s1.split("move ")[1])
		from_stack, to_stack = s2.split(" to ")
		from_stack, to_stack = int(from_stack) - 1, int(to_stack) - 1
		for _ in range(count):
			popped = crate_stacks[from_stack].pop()
			crate_stacks[to_stack].append(popped)
	return "".join(stack[-1] for stack in crate_stacks)

def part2_solution(input: str):
	crate_stacks, rest_of_lines = get_crate_stacks(input)
	crate_stacks, rest_of_lines = get_crate_stacks(input)
	for line in rest_of_lines:
		s1, s2 = line.split("from ")
		count = int(s1.split("move ")[1])
		from_stack, to_stack = s2.split(" to ")
		from_stack, to_stack = int(from_stack) - 1, int(to_stack) - 1
		removed = crate_stacks[from_stack][-count:]
		crate_stacks[to_stack] += removed
		del crate_stacks[from_stack][-count:]
	return "".join(stack[-1] for stack in crate_stacks)

test_input_string = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

file = open("src/input-files/day05-crate-instructions.txt", "r")
input_string = file.read()
file.close()

print("PART 1 ANSWER:", part1_solution(input_string))
print("PART 2 ANSWER:", part2_solution(input_string))