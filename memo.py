import os
import math

def startup():
	cwd = os.getcwd()
	traversal = os.walk(cwd)
	script_dir = cwd + "\\memscripts"

	# Search for all scripts
	for root, dirs, files in traversal:
		if root == script_dir:
			return files

def main():
	memscripts = startup()
	script_num = len(memscripts) + 1

	# Select which script to memorise
	if script_num > len(memscripts):
		print("Which scipt would you like to memorise first?")
		print(*memscripts)
		script_num = int(input(f"Choose from 1~{len(memscripts)}: "))
	
	
	# Loading memscript
	script_name = memscripts[script_num-1]
	script = load(script_name)

	# Tests and writes results onto another file
	results = test(script, script_name)
	eval(results, script_name)

	return 0
	

def load(script):
	script_txt = []

	with open("memscripts/"+script) as test_script:
		for line in test_script:
			line = line.replace('\n', '')
			script_txt.append(line)

	return script_txt

def test(script, script_name):
	incorrect = []

	print(f"Currently testing {script_name}")

	for line in script:
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

def eval(results, script_name):
	try:
		eval_file = open("eval.txt", "x")
	except FileExistsError:
		eval_file = open("eval.txt", "a")
	
	eval_file.write("script_name")

	for line in results:
		eval_file.write(line)
	
	eval_file.write("\n")

	eval_file.close()

startup()
while True:
	main()
	repeat_str = input("Retry?\n")
	if repeat_str.capitalize() in ["YES", "Y"]:
		repeat = True
	else:
		break