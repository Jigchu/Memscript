import os

from memscript.memscript import *
import util.qna as qna
import util.colours as colours
import memscript.memorise as mem
import memo.evaluate as eval

def clear_eval():
	try:
		eval_f = open("eval.txt", "a")
	except FileNotFoundError:
		return 0
	eval_f.seek(0)
	eval_f.truncate(0)
	return 0

def memorise():
	cwd = os.getcwd()
	memscripts = memscript("memscripts", "dir", cwd)
	
	while True:
		script = mem._choose(memscripts)
		if script == None:
			return 0
		repeat = True
		
		while repeat:
			mem._test(script)
			repeat = qna.binary("Do you want to repeat the script?\n")

def view():
	cwd = os.getcwd()
	memscripts = memscript("memscripts", "dir", cwd)
	repeat = True
	
	while repeat:
		script = mem._choose(memscripts)
		if script == None:
			break
		mem._display(script)
		repeat = qna.binary("Would you like to look at another script?\n")

def new_script():
	while True:
		name = input("What do you want to name the script?")
		file_path = os.path.join(os.getcwd(), "memscript", name)
		try:
			script = open(file_path, "x")
		except FileExistsError:
			print(f"{colours.red}File already exists!")
	

# def eval_view():