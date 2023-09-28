import memscript
import qna
import extra

def main():
	# Main menu
	tasks = ["Memorise", "Look at Text", "Clear eval.txt", "Exit"]
	task_functions = {
		1: memscript.memorise,
		2: memscript.view,
		3: extra.clear_eval,
		4: None
	}

	while True:
		task = qna.mcq("What would you like to do?", tasks)
		task = task_functions[task]
		if task == None:
			print("\nBye! :)")
			break
		task()
	
	return 0

try:
	main()
except KeyboardInterrupt:
	print("\nBye! :)")