def top_n_total_calories(calories_list: list[int | None], n: int):
	top_calories_list = [0] * n # guaranteed to be sorted
	current_total_calories: int = 0
	top_calories_sum = 0
	calories_list.append(None)
	for calorie in calories_list:
		if calorie is None:
			for i in range(n):
				if current_total_calories > top_calories_list[i]:
					removed = top_calories_list.pop()
					top_calories_list.insert(i, current_total_calories)
					top_calories_sum += current_total_calories - removed
					break
			current_total_calories = 0
		else:
			current_total_calories += calorie
	assert len(top_calories_list) == n
	return top_calories_sum

def calorie_to_number(s: str):
	if s == "":
		return None
	return int(s)

def part1_solution(input: str):
	calories_list = [calorie_to_number(s) for s in input.split("\n")]
	return top_n_total_calories(calories_list, 1)

def part2_solution(input: str):
	calories_list = [calorie_to_number(s) for s in input.split("\n")]
	return top_n_total_calories(calories_list, 3)

test_input_string = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

tests = {
	test_input_string: (24000, 45000)
}