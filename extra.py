import qna

def clear_eval():
	try:
		eval_f = open("eval.txt", "a")
	except FileNotFoundError:
		return 0
	eval_f.seek(0)
	eval_f.truncate(0)
	return 0