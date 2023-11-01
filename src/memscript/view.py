from memscript.memscript import *

def Display(script: Memscript):
	if script.type == "dir":
		for child in script.children:
			__display(child)
		return
	
	__display(script)
	
	return

def __display(script: Memscript):
	print(f"Currently viewing {script.name}")
	for line in script.script:
		input(line)
	print("\n")
	
	return
