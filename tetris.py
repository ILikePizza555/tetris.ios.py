from scene import *
import sound
import random
import math
A = Action

COLUMNS = 10
ROWS = 20

COLORS = {
	"bg": "#232323",
	"red": "#FF5555",
	"grey": "#646473",
	"blue": "#786CF5",
	"orange": "#FF8C32",
	"green": "327834",
	"lime": "92CA49",
}

class TetrisGame (Scene):
	"""
	The main game code for Tetris
	"""
	def setup(self):
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(TetrisGame(), PORTRAIT, show_fps=False) 
