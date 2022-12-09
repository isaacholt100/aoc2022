def files_and_dirs(input: str):
	directories = ["/"]
	current_directory = ""
	files = []
	for line in input.split("\n"):
		is_command = line.startswith("$")
		if is_command:
			spl = line.split(" ")
			command = spl[1]
			if command == "cd":
				next_directory = spl[2]
				if next_directory == "..":
					current_directory = "/".join(current_directory.split("/")[:-2]) + "/"
				elif next_directory == "/":
					current_directory = next_directory
				else:
					current_directory += next_directory + "/"
			else:
				assert command == "ls"
			#print(command)
		else:
			if line.startswith("dir"):
				directories.append(current_directory + line.split(" ")[1] + "/")
			else:
				spl = line.split(" ")
				files.append({ "name": spl[1], "size": int(spl[0]), "location": current_directory })
	return (files, directories)

def part1_solution(input: str):
	files, directories = files_and_dirs(input)
	total = 0
	for dir in directories:
		dir_size = 0
		for file in files:
			if file["location"].startswith(dir):
				dir_size += file["size"]
		if dir_size <= 100000:
			total += dir_size
	return total

def part2_solution(input: str):
	files, directories = files_and_dirs(input)
	root_size = sum(file["size"] for file in files)
	total_space = 70000000
	required_space = 30000000
	min_dir_size = root_size
	for dir in directories:
		dir_size = 0
		for file in files:
			if file["location"].startswith(dir):
				dir_size += file["size"]
		if total_space - (root_size - dir_size) >= required_space:
			if dir_size < min_dir_size:
				min_dir_size = dir_size
	
	return min_dir_size

test_input_string = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

tests = {
	test_input_string: (95437, 24933642)
}