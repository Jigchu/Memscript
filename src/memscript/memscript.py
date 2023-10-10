import os

class memscript:
	def __init__(self, name: str, type: str, parent: str):
		self.name = name
		self.type = type if type in ["dir", "file"] else "file"
		self.parent = parent
		self.children = []
		if self.type == "dir":
			self.children = self.__get_children()
		self.script = self.__load()

	def __get_children(self):
		start_dir = os.path.join(self.parent, self.name)
		traversal = os.walk(start_dir)
		children = []

		for root, dirs, files in traversal:
			for dir in dirs:
				children.append(memscript(dir, "dir", root))
			for file in files:
				children.append(memscript(file, "file", root))

		return children

	def __load(self):
		script = []

		if self.type == "dir":
			return script

		with open(os.path.join(self.parent, self.name), encoding="UTF-8") as script_f:
			for line in script_f:
				line = line.replace('\n', '')
				script.append(line)
		return script