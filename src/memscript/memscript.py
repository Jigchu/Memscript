import os
import util.cd as cd

class memscript:
	def __init__(self, name: str, type: str, parent: str):
		self.name = name
		self.type = type if type in ["dir", "file"] else "file"
		self.parent = parent
		self.children: list[memscript] = []
		if self.type == "dir":
			self.children = self.__get_children()
		self.script = self.__load()

	@classmethod
	def init_root(memscript):
		path = cd.find("memscripts", "dir", "memo")
		parent, name = os.path.split(path)
		return memscript(name, "dir", parent)

	def update(self):
		for child in self.children:
			dir = child.type == "dir"
			if dir:
				child.update()
				continue
			path = os.path.join(child.parent, child.name)
			try:
				open(path)
			except FileNotFoundError:
				self.children.remove(child)

	def filter(self, func: function):
		return

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
		with open(os.path.join(self.parent, self.name)) as script_f:
			for line in script_f:
				line = line.replace('\n', '')
				script.append(line)
		return script