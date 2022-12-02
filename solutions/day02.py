from enum import IntEnum

class Shape(IntEnum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

	def from_char(s: str):
		if s == "A" or s == "X":
			return Shape.ROCK
		if s == "B" or s == "Y":
			return Shape.PAPER
		if s == "C" or s == "Z":
			return Shape.SCISSORS
		raise "Attempt to convert invalid string to Shape"

	def score(self, opponent):
		shape_score = int(self)
		opponent_shape_score = int(opponent)
		outcome_score = 0
		if shape_score == opponent_shape_score:
			outcome_score = 3
		else:
			diff = shape_score - opponent_shape_score
			if diff == 1 or diff == -2:
				outcome_score = 6
		return outcome_score + shape_score

strategy_file = open("input-files/day02-rps-strategy.txt", "r")
strategy_string = strategy_file.read()
strategy_file.close()
print("PART 1 ANSWER:", sum([Shape.from_char(s[2]).score(Shape.from_char(s[0])) for s in strategy_string.split("\n")]))