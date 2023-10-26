from rich import print
from rich.layout import Layout
from rich.console import Console
from pynput import keyboard

MIN_SIZE = 3

def set_layout():
	layout = Layout(name="root")

	layout.split(
		Layout(name="header", size=MIN_SIZE),
		Layout(name="body", minimum_size=5),
		Layout(name="footer", size=MIN_SIZE),
	)

	return layout

if __name__ == "__main__":
	print(set_layout())