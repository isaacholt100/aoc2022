import sys

sys.path.append("../src")

def read_file_string(name: str):
	file = open("src/input-files/" + name, "r")
	s = file.read()
	file.close()
	return s