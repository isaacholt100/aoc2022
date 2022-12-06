def find_common_item_priority(s: str):
	assert len(s) % 2 == 0
	half = len(s) // 2
	first = s[0:half]
	second = s[half:]
	chars_set = set()
	for c in first:
		chars_set.add(c)
	for c in second:
		if c in chars_set:
			return priority(c)
	raise BaseException("no common items found")
	
def priority(s: str):
	o = ord(s)
	if o <= 90 and o >= 65:
		return o - 38
	if o <= 122 and o >= 97:
		return o - 96
	raise BaseException("letter expected")

def part_1_solution(input: str):
	return sum(find_common_item_priority(s) for s in input.split("\n"))

def find_common_item_priority_in_list(items_list: list[str]):
	assert len(items_list) > 1
	print(items_list)
	chars_dict = dict()
	chars_set = set()
	for c in items_list[0]:
		chars_set.add(c)
	for s in items_list[1:]:
		new_chars_set = set()
		for c in s:
			new_chars_set.add(c)
		chars_set = chars_set.intersection(new_chars_set)
	return priority(chars_set.pop())

def part_2_solution(input: str):
	lines = input.split("\n")
	assert len(lines) % 3 == 0
	return sum(find_common_item_priority_in_list(lines[(3 * i):(3 * i + 3)]) for i in range(len(lines) // 3))

file = open("src/input-files/day03-rucksack-items.txt", "r")
rucksack_items_string = file.read()
file.close()

test_input_string = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

assert part_1_solution(test_input_string) == 157
print("PART 1 ANSWER:", part_1_solution(rucksack_items_string))

print("PART 2:", part_2_solution(rucksack_items_string))