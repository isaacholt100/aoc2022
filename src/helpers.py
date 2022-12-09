class TestCases:
	def __init__(self, cases: dict):
		self.cases = cases
	
	def run_tests(self, part1_fn, part2_fn):
		for key, val in self.cases.items():
			if part2_fn is not None:
				assert val[0] == None or part1_fn(key) == val[0]
				assert val[1] == None or part2_fn(key) == val[1]
			else:
				assert part1_fn(key) == val
	
class Solutions:
	def __init__(self, file_name: str, cases: dict):
		file = open("src/input-files/" + file_name, "r")
		input_string = file.read()
		file.close()
		self.input = input_string
		self.cases = TestCases(cases)

	def print_answers(self, part1_fn, part2_fn = None, check_answers = None):
		print("running tests...")
		self.cases.run_tests(part1_fn, part2_fn)
		print("tests passed succesfully"),

		part1_answer = part1_fn(self.input)
		part2_answer = part2_fn(self.input) if part2_fn is not None else None
		if check_answers is not None:
			print("running custom check of answers...")
			assert check_answers(part1_answer, part1_answer)
		print("PART 1 ANSWER:", part1_answer)
		if part2_fn is not None:
			print("PART 2 ANSWER:", part2_answer)