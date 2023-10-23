import pynput

from memscript.memscript import *
import util.qna as qna

def Edit():
	script = __location()
	if script == None:
		return
	__edit(script)

def __location():
	memscripts = memscript.init_root()
	files = memscripts.get_children()
	options = [file.name for file in files if file.type == "file"]

	result = qna.mcq("Where would you like to create your new script?", options)
	
	back = result == -1
	if back:
		return None
	
	script = files[result - 1]
	
	return script

def __edit(memscript: memscript):
	script = memscript.script

	for line in script:
		__edit_line()

	return

def __edit_line(line: str):

	return