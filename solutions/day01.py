def top_n_total_calories(calories_list: list[int | None], n: int):
	top_calories_list = [0] * n # guaranteed to be sorted
	current_total_calories: int = 0
	top_calories_sum = 0
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

calories_file = open("input-files/day01-elf-calories.txt", "r")
calories_string: str = calories_file.read()
calories_file.close()

calories_list = [calorie_to_number(s) for s in calories_string.split("\n")]
max_total_calories: int = 0
current_total_calories: int = 0
for c in calories_list:
	if c is None:
		if current_total_calories > max_total_calories:
			max_total_calories = current_total_calories
		current_total_calories = 0
	else:
		current_total_calories += c

part1 = top_n_total_calories(calories_list, 1)
print("PART 1 ANSWER:", part1)

part2 = top_n_total_calories(calories_list, 3)
assert 3 * part1 >= part2
print("PART 2 ANSWER:", part2)