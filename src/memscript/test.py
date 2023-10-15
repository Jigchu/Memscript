from memscript.memscript import *
import util.colours as colours
import evaluate as eval

def test(script: memscript):
	if script.type == "dir":
		print(f"Currently memorising set of scripts under {script.name}")
		for child in script.children:
			test(child)
		return
	
	results = __test(script)
	
	if "q" in results:
		return

	eval.evaluate(results, script)
	return

def __test(script: memscript):
	incorrect = set()
	skipped = 0

	print(f"Currently testing {script.name}")

	for line in script.script:
		correct = False
		while not correct:
			input_buffer = input().strip()

			result = __mark(input_buffer, line)
			if result == -1:
				print("\n")
				return ["q"]
			if result == -2:
				print("\n")
				return ["Script skipped"]
			if result == -3:
				correct = True
				skipped += 1
			if result == 1:
				correct = True
				continue
			incorrect.add(line)

	print("\n")
	print(f"{len(script.script) - len(incorrect)}/{len(script.script)} lines correct")
	print(f"{skipped}/{len(script.script)} lines skipped")

	return incorrect

def __mark(input_buffer: str, line: str):
	marks = 0
	quit = input_buffer.lower() == "q"
	skip = input_buffer.lower() == "s"
	continued = input_buffer.lower() == "c"

	if input_buffer == line:
		marks = 1
	elif quit:
		marks = -1
	elif skip:
		marks = -2
	elif continued:
		marks = -3
	
	if marks == 0:
		remarks: tuple[str] = __check(input_buffer, line)
		print(remarks[0])
		print(remarks[1])

	return marks


def __check(input_buffer: str, line: str):
	lines = (input_buffer.split(), line.split())
	remarks = [f"{colours.red}Incorrect Response: {colours.reset}", f"{colours.cyan}Correct Response: {colours.reset}"]
	right = __right(lines)
	
	buffer = list(lines)
	for c_word in right:
		i_index = buffer[0].index(c_word)
		c_index = buffer[1].index(c_word)
		wrong = [
			[word for word in buffer[0][:i_index if i_index > 0 else 0]], 
			[word for word in buffer[1][:c_index if c_index > 0 else 0]],
		]

		remarks[0] += colours.red
		remarks[1] += colours.cyan
		for word in wrong[0]:
			remarks[0] += word + " "
		for word in wrong[1]:
			remarks[1] += word + " "
		remarks[0] += colours.reset + buffer[0][i_index] + " "
		remarks[1] += colours.reset + buffer[1][c_index] + " "

		buffer[0] = buffer[0][i_index + 1:] if i_index < len(buffer[0]) - 1 else []
		buffer[1] = buffer[1][c_index + 1:] if c_index < len(buffer[1]) - 1 else []
	
	remarks[0] += colours.red
	remarks[1] += colours.cyan

	for word in buffer[0]:
		remarks[0] += word + " "
	for word in buffer[1]:
		remarks[1] += word + " "

	remarks[0] += colours.reset
	remarks[1] += colours.reset

	return tuple(remarks)


def __right(lines: tuple[str]):
	right = []
	buffer = lines[0]
	previous_index = 0

	for word in lines[1]:
		idx = previous_index
		for iword in buffer:
			if word == iword:
				if idx < previous_index:
					continue
				previous_index = idx
				right.append(word)
				buffer = lines[0][idx + 1:] if idx < len(lines[0]) - 1 else []
				break
			idx += 1
	
	return right