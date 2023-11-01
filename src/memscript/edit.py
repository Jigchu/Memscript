from pynput.keyboard import Controller
from multiprocessing import Process, Pipe
from time import sleep
import os

from memscript.memscript import *
import util.qna as qna
import util.colours as colours

def Edit():
	script = __location()
	if script == None:
		return
	__edit(script)

def __location():
	memscripts = Memscript.init_root()
	files = memscripts.get_children()
	options = [file.name for file in files if file.type == "file"]

	result = qna.mcq("Which script would you like to edit?", options)
	
	back = result == -1
	if back:
		return None
	
	script = files[result]
	
	return script

def __edit(memscript: Memscript):
	script = memscript.script
	finished = False
	new_script = []

	print(f"{colours.green}You are now editing {memscript.name}!")
	print(f"Edit line by line and press enter once you are done with the current line.")
	print(f"Press 'w' once you have completed all your edits{colours.reset}") 

	for line in script:
		print(f"Original line: {line}")
		
		parent_conn, child_conn = Pipe()
		sub_proc = Process(target=__write_stdin, args=(child_conn, line,))
		sub_proc.start()
		parent_conn.send([True])
		new_line = input().strip()
		sub_proc.join()

		if new_line == "w":
			finished = True
			break

		new_script.append(new_line)

	print(f"{colours.green}You are now adding lines to {memscript.name}{colours.reset}")

	while not finished:
		line = input().strip()
		write = line.lower() == "w"
		if write:
			break
		new_script.append(line)

	with open(os.path.join(memscript.parent, memscript.name), "w") as script_file:
		for line in new_script:
			script_file.write(line + "\n")

	return

def __write_stdin(conn, line: str):
	ran = conn.recv()[0]
	sleep(0.01)
	kbd = Controller()
	if ran:
		kbd.type(line)
	return 0