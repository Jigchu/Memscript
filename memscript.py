import os
import time
import qna

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
		start_dir = os.path.join(self.parent, self.name)
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

		with open(os.path.join(self.parent, self.name)) as script_f:
			for line in script_f:
				line = line.replace('\n', '')
				script.append(line)
		return script

def memorise():
	cwd = os.getcwd()
	memscripts = memscript("memscripts", "dir", cwd)
	repeat = True
	
	script = choose(memscripts)
	
	while repeat:
		test(script)
		repeat = qna.binary("Do you want to repeat the script?\n")

	return 0
	
def choose(memscripts: memscript):
	scripts = ["All"]
	num_script = len(memscripts.children) + 1
	chosen_script = num_script + 1
	deeper = False
	script = None

	for child in memscripts.children:
		scripts.append(child.name)
	
	chosen_script = qna.mcq("Which script would you like to memorise", scripts)

	chosen_script -= 1

	if chosen_script == 0:
		script = memscripts
	else:
		script: memscript = memscripts.children[chosen_script - 1]

	return script


def test(script: memscript):
	if script.type == "dir":
		print(f"Currently set of scripts under {script.name}")
		for child in script.children:
			test(child)
		return
	
	results = _test(script)
	_evaluate(results, script)

	return

def _test(script: memscript):
	incorrect = []

	print(f"Currently testing {script.name}")

	for line in script.script:
		correct = False
		while not correct:
			input_buffer = input()
			if input_buffer.lower() == "q":
				return []
			if input_buffer == line:
				correct = True
				continue
			print(f"Incorrect Response: {input_buffer}")
			print(f"Correct Response: {line}")
			incorrect.append(line)

	return incorrect

def _evaluate(results, script: memscript):
	try:
		eval_file = open("eval.txt", "x")
	except FileExistsError:
		eval_file = open("eval.txt", "a")

	eval_file.write(f"{script.name} {time.asctime()}\n")

	if results == []:
		eval_file.write("No mistakes\n")

	for line in results:
		eval_file.write(line + "\n")

	eval_file.close()