def get_marker(input: str, length: int):
	assert length > 0
	current_sub_str = ""
	for i, char in enumerate(input):
		index = current_sub_str.find(char)
		if index != -1:
			current_sub_str = current_sub_str[index + 1:]
		current_sub_str += char
		if len(current_sub_str) == length:
			return i + 1
	raise BaseException("no marker found")

def part1_solution(input: str):
	return get_marker(input, 4)

def part2_solution(input: str):
	return get_marker(input, 14)

tests = {
	"mjqjpqmgbljsphdztnvjfqwrcgsmlb": (7, 19),
	"bvwbjplbgvbhsrlpgdmjqwftvncz": (5, 23),
	"nppdvjthqldpwncqszvftbrmjlhg": (6, 23),
	"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": (10, 29),
	"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": (11, 26),
}