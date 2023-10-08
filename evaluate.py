from memscript import *
import time

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

def __eval_display():
	entries: list[list[str]] = __format_eval__
	

def __format_eval__():
	try:
		eval_f = open("eval.txt", "r")
	except FileNotFoundError:
		print("eval.txt does not exist")
		return -1
	
	