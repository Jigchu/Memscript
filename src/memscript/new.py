import os

from memscript.memscript import *
import util.cd as cd
import util.qna as qna
import util.colours as colours

def Add(root: str):
	root = __location(root)
	if root == "":
		return
	path = __name(root)
	__write(path)

def __location(root: str):
	memdirs = memscript.init_root()
	
	dir: callable[memscript, bool] = lambda child: child.type == "dir"

	memdirs.filter(dir)
	dirs = memdirs.get_children()
	dirs.insert(0, memdirs)
	options = [d.name for d in dirs]
	for idx, option in enumerate(options):
		if option == root and option != "Memscripts":
			options[idx] = option + " (Recently made)"

	result = qna.mcq("Where would you like to create your new script?", options)
	
	back = result == -1
	if back:
		return ""
	
	script = dirs[result - 1]
	root = script.name

	return root

def __name(root: str):
	dir = qna.binary(f"Would you like to create a new directory in {root}?\n")
	prompt = "What would you like to name the new script?\n" if not dir else "What would you like to name the new directory?\n"
	name = input(prompt)
	name += ".txt" if not dir else ""
	path = os.path.join(cd.find(root, "dir", "memo"), name)

	return path

def __write(path: str):
	if ".txt" not in path:
		try:
			os.mkdir(path)
		except FileExistsError or FileNotFoundError:
			print(f"{colours.red}Could not create directory!{colours.reset}")
			return
		print(f"{colours.green}Directory successfully created!{colours.reset}")
		prev_dir, curr_dir = os.path.split(path)
		Add(curr_dir)
		return
		
	try:
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