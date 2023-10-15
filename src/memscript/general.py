import os

from memscript.memscript import *
import evaluate as eval
import util.qna as qna
import util.colours as colours

def choose(memscripts: memscript):
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