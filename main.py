import qna
import features

def main():
	# Main menu
	tasks = ["Memorise", "Look at Text", "Clear eval.txt", "View eval.txt", "Exit"]
	task_functions = {
		1: features.memorise,
		2: features.view,
		3: features.clear_eval,
		4: features.eval_view,
		5: None,
	}

	while True:
		task = qna.mcq("What would you like to do?", tasks, False)
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