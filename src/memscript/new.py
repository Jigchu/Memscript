import os
import util.cd as cd
import util.qna as qna
import util.colours as colours

def add_script(root: str):
	path = name(root)
	write(path)

def name(root: str):
	dir = qna.binary("Would you like to create a new directory?\n")
	prompt = "What would you like to name the new script?\n" if not dir else "What would you like to name the new directory?\n"
	name = input(prompt)
	name += ".txt" if not dir else ""
	path = os.path.join(cd.find(root, "dir", "memo"), name)

	return path

def write(path: str):
	if ".txt" not in path:
		try:
			os.mkdir(path)
		except FileExistsError or FileNotFoundError:
			print(f"{colours.red}Could not create directory!{colours.reset}")
			return
		print(f"{colours.green}Directory successfully created!{colours.reset}")
		prev_dir, curr_dir = os.path.split(path)
		add_script(curr_dir)
		return
		
	try:
		print(path)
		script_file = open(path, "x")
	except FileExistsError:
		print(f"{colours.red}File already exists! Try editing the file instead.{colours.reset}")
		return
	
	script = []

	print("You are now creating a new script!")
	print("Simply type in the contents line by line separating each by pressing enter.")
	print(f"{colours.green}You can start typing{colours.reset}")
	
	while True:
		line = input().strip()
		
		retry = line.lower() == "r"
		write = line.lower() == "w"
		if write:
			break
		elif retry:
			script.pop()
			continue

		script.append(line)

	for line in script:
		script_file.write(line + "\n")
	
	script_file.close()
	return