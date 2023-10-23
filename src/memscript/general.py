import os

from memscript.memscript import *
import evaluate as eval
import util.qna as qna
import util.colours as colours

def choose(memscripts: memscript, all: bool = True):
	scripts = []
	if all:
		scripts.append("All")
	script = None

	for child in memscripts.children:
		scripts.append(child.name)
	
	if not all:
		scripts.insert(0, memscripts.name)

	chosen_script = qna.mcq("Which script would you like to choose", scripts)

	if chosen_script == -1:
		return None

	chosen_script -= 1

	if chosen_script == 0:
		script = memscripts
	else:
		script: memscript = memscripts.children[chosen_script - 1]

	return script