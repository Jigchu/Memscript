from src.memscript.memscript import *

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
