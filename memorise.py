import os
import time

from memscript import *
import qna
import colours

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
	script = None

	for child in memscripts.children:
		scripts.append(child.name)
	
	chosen_script = qna.mcq("Which script would you like to choose", scripts)

	if chosen_script == -1:
		return None

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
	incorrect = set()

	print(f"Currently testing {script.name}")

	for line in script.script:
		correct = False
		while not correct:
			input_buffer = input().strip()

			result = _mark(input_buffer, line)
			if result == -1:
				print("\n")
				return ["Script skipped"]
			if result == 1:
				correct = True
				continue
			incorrect.add(line)

	print("\n")
	print(f"{len(script.script) - len(incorrect)}/{len(script.script)} lines correct")

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
	lines = (input_buffer.split(), line.split())
	remarks = [f"{colours.red}Incorrect Response: {colours.reset}", f"{colours.cyan}Correct Response: {colours.reset}"]
	right = []
	buffer = lines[0]
	previous_index = 0
	prev_max_idx = 0

	for word in lines[1]:
		idx = prev_max_idx
		for iword in buffer:
			if word == iword:
				if idx < previous_index:
					continue
				previous_index = idx
				right.append(word)
				buffer = lines[0][idx + 1:] if idx < len(lines[0]) - 1 else []
				prev_max_idx = idx
				break
			idx += 1
	
	buffer = list(lines)
	for c_word in right:
		i_index = buffer[0].index(c_word)
		c_index = buffer[1].index(c_word)
		wrong = [
			[word for word in buffer[0][:i_index if i_index > 0 else 0]], 
			[word for word in buffer[1][:c_index if c_index > 0 else 0]],
		]

		remarks[0] += colours.red
		remarks[1] += colours.cyan
		for word in wrong[0]:
			remarks[0] += word + " "
		for word in wrong[1]:
			remarks[1] += word + " "
		remarks[0] += colours.reset + buffer[0][i_index] + " "
		remarks[1] += colours.reset + buffer[1][c_index] + " "

		buffer[0] = buffer[0][i_index + 1:] if i_index < len(buffer[0]) - 1 else []
		buffer[1] = buffer[1][c_index + 1:] if c_index < len(buffer[1]) - 1 else []
	
	remarks[0] += colours.red
	remarks[1] += colours.cyan

	for word in buffer[0]:
		remarks[0] += word + " "
	for word in buffer[1]:
		remarks[1] += word + " "

	remarks[0] += colours.reset
	remarks[1] += colours.reset

	return tuple(remarks)

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
	
	eval_file.write("\n")

	eval_file.close()