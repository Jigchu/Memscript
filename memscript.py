import os

class memscript:
	def __init__(self, name: str, type: str, parent: str):
		self.name = name
		self.type = type if type in ["dir", "file"] else "file"
		self.parent = parent
		self.children = []
		if self.type == "dir":
			self.children = self.__get_children()
		self.script = self.__load()

	def __get_children(self):
		start_dir = self.parent + f"\\{self.name}"
		traversal = os.walk(start_dir)
		children = []
		
		for root, dirs, files in traversal:
			for dir in dirs:
				children.append(memscript(dir, "dir", root))
			for file in files:
				children.append(memscript(file, "file", root))
		
		return children
	
	def __load(self):
		script = []
		
		if self.type == "dir":
			return script

		with open(self.parent + "\\" + self.name) as script_f:
			for line in script_f:
				line = line.replace('\n', '')
				script.append(line)
		return script
	
def main():
	cwd = os.getcwd()
	memscripts = memscript("memscripts", "dir", cwd)
	num_of_script = len(memscripts.children)
	chosen_script = num_of_script + 1

	if chosen_script > num_of_script:
		print("Which scipt would you like to memorise first?")
		print(*memscripts.children)
		script_num = int(input(f"Choose from 1~{len(memscripts.children)}: "))

def test(script: memscript):
	return []

def _test(script: memscript):
	incorrect = []

	print(f"Currently testing {script.name}")

	for line in script.script:
		correct = False
		while not correct:
			input_buffer = input()
			if input_buffer == line:
				correct = True
				continue
			print(f"Incorrect Response: {input_buffer}")
			print(f"Correct Response: {line}")
			incorrect.append(line)
	
	return incorrect

def eval(results, script: memscript):
	try:
		eval_file = open("eval.txt", "x")
	except FileExistsError:
		eval_file = open("eval.txt", "a")
	
	eval_file.write("script_name")

	for line in results:
		eval_file.write(line)
	
	eval_file.write("\n")

	eval_file.close()