import os

class cd:
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)

def find_dir(search: str, root: str):
	root_dir = __root(root)
	walk_object = os.walk(root_dir)

	for r, dirs, files in walk_object:
		for dir in dirs:
			if dir == search:
				return os.path.join(r, dir)

def __root(root: str):
	cwd = os.getcwd()
	prev_dir = cwd
	curr_dir = None
	
	while curr_dir != root or curr_dir != "":
		prev_dir, curr_dir = os.path.split(prev_dir)
	
	return os.path.join(prev_dir, curr_dir)