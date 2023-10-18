import shutil
import os

from memscript.memscript import *
import memscript.general as gen
import memscript.test as test
import memscript.view as view
import memscript.new as new
import util.qna as qna
import util.colours as colours
import evaluate as eval

def clear_eval():
	try:
		eval_f = open("eval.txt", "a")
	except FileNotFoundError:
		return 0
	eval_f.seek(0)
	eval_f.truncate(0)
	return 

def memorise():
	memscripts = memscript.init_root()

	while True:
		script = gen.choose(memscripts)
		if script == None:
			return 
		repeat = True
		
		while repeat:
			test.test(script)
			repeat = qna.binary("Do you want to repeat the script?\n")

def view():
	memscripts = memscript.init_root()
	repeat = True
	
	while repeat:
		script = gen.choose(memscripts)
		if script == None:
			break
		view.display(script)
		repeat = qna.binary("Would you like to look at another script?\n")

def new_script():
	create = True

	while create:
		new.add_script("Memscripts")
		create = qna.binary("Do you want to create another script or directory?\n")
	
	return

def edit_script():
	edit = True
	while edit:
		edit = qna.binary("Do you want to edit another script or directory?\n")
	
	return

def del_script():
	memscripts = memscript.init_root()
	delete = True
	while delete:
		script = gen.choose(memscripts)
		if script == None:
			break
		path = os.path.join(script.parent, script.name)
		comfirm = qna.binary(f"{colours.red}Are you sure you want to remove {script.name} permanently?{colours.reset}\n")
		if not comfirm:
			break
		dir = script.type == "dir"
		shutil.rmtree(path) if dir else os.remove(path)
		delete = qna.binary("Do you want to delete another script or directory?\n")
		if delete:
			memscripts.update()
	return

def eval_view():
	return