import os
import time
import qna
import colours

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
	
	script = _choose(memscripts)
	
	while repeat:
		_test(script)
		repeat = qna.binary("Do you want to repeat the script?\n")

	return 0

def view():
	cwd = os.getcwd()
	memscripts = memscript("memscripts", "dir", cwd)
	repeat = True
	
	while repeat:
		script = _choose(memscripts)
		_display(script)
		repeat = qna.binary("Would you like to look at another script?\n")
	
def _display(script: memscript):
	if script.type == "dir":
		for child in script.children:
			__display(child)
		return
	
	__display(script)
	
	return

def __display(script: memscript):
	print(f"Currently viewing {script.name}")
	for line in script.script:
		input(line)
	print("\n")
	
	return

def _choose(memscripts: memscript):
	scripts = ["All"]
	num_script = len(memscripts.children) + 1
	chosen_script = num_script + 1
	deeper = False
	script = None

	for child in memscripts.children:
		scripts.append(child.name)
	
	chosen_script = qna.mcq("Which script would you like to choose", scripts)

	chosen_script -= 1

	if chosen_script == 0:
		script = memscripts
	else:
		script: memscript = memscripts.children[chosen_script - 1]

	return script

def _test(script: memscript):
	if script.type == "dir":
		print(f"Currently memorising set of scripts under {script.name}")
		for child in script.children:
			_test(child)
		return
	
	results = __test(script)
	_evaluate(results, script)

	return

def __test(script: memscript):
	incorrect = []

	print(f"Currently testing {script.name}")

	for line in script.script:
		correct = False
		while not correct:
			input_buffer = input()
			result = _mark(input_buffer, line)
			if result == -1:
				print("\n")
				return []
			if result == 1:
				correct = True
				continue
			incorrect.append(line)

	print("\n")

	return incorrect

def _mark(input_buffer: str, line: str):
	marks = 0
	if input_buffer == line:
		marks = 1
	elif input_buffer.lower() == "q":
		marks = -1
	
	if marks == 0:
		remarks: tuple[str] = _check(input_buffer, line)
		print(remarks[0])
		print(remarks[1])

	return marks

def _check(input_buffer: str, line: str):
	incorrect = colours.red + "Incorrect Response: " + colours.reset
	correct = colours.cyan + "Correct Response: " + colours.reset
	wrong = False
	index = 0
	
	for idx, char in enumerate(input_buffer):
		if char == line[idx]:
			wrong = False
			incorrect += colours.reset
			correct += colours.reset

		if char != line[idx]:
			wrong = True
			incorrect += colours.red
			correct += colours.cyan
		
		incorrect += char
		correct += line[idx]
		index = idx
	
	incorrect += colours.red
	incorrect += line[idx + 1:] if len(line) > len(input_buffer) else ""
	correct += colours.cyan + colours.reset
	
	return (incorrect, correct)
			

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