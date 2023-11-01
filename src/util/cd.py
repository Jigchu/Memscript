import os

class cd:
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)

def find(search: str, type: str, root: str):
	dir = 1 if type == "dir" else 0 if type == "file" else -1
	if dir == -1:
		return ""
	root_dir = __root(root)
	walk_object = os.walk(root_dir)
	path = ""

	for r, dirs, files in walk_object:
		for item in dirs if dir == 1 else files:
			if item == search:
				path = os.path.join(r, search)
	return path

def __root(root: str):
	cwd = os.getcwd()
	prev_dir = cwd
	curr_dir = None
	
	while True:
		prev_dir, curr_dir = os.path.split(prev_dir)
		if curr_dir == root or curr_dir == "":
			break

	return os.path.join(prev_dir, curr_dir)