import memscript
import qna
import extra

def main():
	# Main menu
	tasks = ["Memorise", "Clear eval.txt"]

	task = qna.mcq("What would you like to do?", tasks)

	if task == 2:
		extra.clear_eval()

	memscript.memorise()

	return 0

try:
	main()
except KeyboardInterrupt:
	print("\nBye! :)")