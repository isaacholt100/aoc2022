from typing import Callable
from operator import mul
from functools import reduce

class MonkeyRule:
	id: int
	items: list[int]
	operation: Callable[[int], int]
	divisible_test: int
	next_monkey_if_true: int
	next_monkey_if_false: int

	def __init__(self, note: str):
		lines = note.split("\n")
		self.id = int(lines[0].split("Monkey ")[1].split(":")[0])
		starting_items = [int(item) for item in lines[1].split("  Starting items: ")[1].split(", ")]
		self.items = starting_items
		op, operand = lines[2].split("  Operation: new = old ")[1].split(" ")
		if operand == "old":
			self.operation = lambda old: old * old
		else:
			operand = int(operand)
			if op == "+":
				self.operation = lambda old: old + operand
			else:
				self.operation = lambda old: old * operand
		self.divisible_test = int(lines[3].split("  Test: divisible by ")[1])
		self.next_monkey_if_true = int(lines[4].split("    If true: throw to monkey ")[1])
		self.next_monkey_if_false = int(lines[5].split("    If false: throw to monkey ")[1])

	def execute(self, monkey_rules, div3 = True):
		while len(self.items) != 0:
			worry_level = self.items.pop(0)
			worry_level = self.operation(worry_level)
			if div3:
				worry_level = worry_level // 3
			next_index = self.next_monkey_if_true if worry_level % self.divisible_test == 0 else self.next_monkey_if_false
			monkey_rules[next_index].items.append(worry_level)
			
	def execute2(self, monkey_rules, p = int):
		while len(self.items) != 0:
			worry_level = self.items.pop(0)
			worry_level = self.operation(worry_level)
			next_index = self.next_monkey_if_true if worry_level % self.divisible_test == 0 else self.next_monkey_if_false
			worry_level = worry_level % p
			monkey_rules[next_index].items.append(worry_level)

def max2(ls: list[int]):
	m1, m2 = ls[0], ls[0]
	for item in ls:
		if item > m1:
			m1, m2 = item, m1
		elif item > m2:
			m2 = item
	return m1, m2

def part1_solution(input: str):
	notes = input.split("\n\n")
	monkey_rules = [MonkeyRule(note) for note in notes]
	inspection_counts = [0] * len(notes)
	for r in range(20):
		for rule in monkey_rules:
			inspection_counts[rule.id] += len(rule.items)
			rule.execute(monkey_rules)
	max_inspections = max2(inspection_counts)
	return max_inspections[0] * max_inspections[1]

def part2_solution(input: str):
	notes = input.split("\n\n")
	monkey_rules = [MonkeyRule(note) for note in notes]
	inspection_counts = [0] * len(notes)
	p = reduce(mul, (rule.divisible_test for rule in monkey_rules), 1)
	for r in range(10000):
		for rule in monkey_rules:
			inspection_counts[rule.id] += len(rule.items)
			rule.execute2(monkey_rules, p)
	max_inspections = max2(inspection_counts)
	return max_inspections[0] * max_inspections[1]

test_input_string = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

tests = {
	test_input_string: (10605, None)
}