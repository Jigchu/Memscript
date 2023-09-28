def binary(prompt: str):
	response = ""
	result = None

	while result == None:
		response = input(prompt)
		response = response.lower()
		if "y" in response:
			result = True
		elif "n" in response:
			result = False
	
	return result

def mcq(prompt: str, items: list[str]):
	item_num = len(items)
	answer = item_num + 1
	print(prompt)
	print(__mcq_format(items))

	while answer > item_num:
		try:
			answer = int(input(f"Choose from 1~{item_num}: "))
		except ValueError:
			print("Invalid input")
	
	return answer

def __mcq_format(items: list[str]):
	fstring = ""
	
	for index, item in enumerate(items):
		fstring += f"{index + 1}: {item}    "
	
	return fstring