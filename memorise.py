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
			input_buffer = input().strip()

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
	input_buffer = input_buffer.split()
	input_list = input_buffer
	line = line.split()
	incorrect = colours.red + "Incorrect Response: " + colours.reset
	correct = colours.cyan + "Correct Response: " + colours.reset
	right = []

	for word in line:
		for input_word in input_list:
			if word == input_word:
				right.append(input_word)
				try:
					input_list = input_list[input_list.index(input_word) + 1:]
				except IndexError:
					input_list = []
				break
	
	for word in line:
		try:
			right.index(word)
		except ValueError:
			correct += colours.cyan
		correct += word + " "
		correct += colours.reset
	
	for word in input_buffer:
		try:
			right.index(word)
		except ValueError:
			incorrect += colours.red
		incorrect += word + " "
		incorrect += colours.reset

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
	
	eval_file.write("\n")

	eval_file.close()