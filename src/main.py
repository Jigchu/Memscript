import util.qna as qna
import features as features

def main():
	# Main menu
	tasks = ["Exit", "Memorise", "Look at Text", "Add Text", "Clear eval.txt", "View eval.txt"]
	task_functions = {
		0: None,
		1: features.memorise,
		2: features.view,
		3: features.new_script,
		4: features.edit_script,
		5: features.clear_eval,
		6: features.eval_view,
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