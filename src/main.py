if __name__ == "__main__":
	day = input("Enter day number to print answers for that day (must be two digits): ")
	
	import importlib
	mod = importlib.import_module("solutions.day" + day)

	from helpers import Solutions

	s = Solutions("day" + day + ".txt", mod.tests)
	if "part2_solution" in dir(mod):
		s.print_answers(mod.part1_solution, mod.part2_solution)
	else:
		s.print_answers(mod.part1_solution)