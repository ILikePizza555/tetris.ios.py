from scene import *
from ui import Path
import sound
import random
import math
A = Action

COLUMNS = 10
ROWS = 20

GRID_POS = Vector2(10, 20);
GRID_SIZE= 10;

COLORS = {
	"bg": "#232323",
	"red": "#FF5555",
	"grey": "#646473",
	"blue": "#786CF5",
	"orange": "#FF8C32",
	"green": "327834",
	"lime": "92CA49",
}

def build_background_grid():
	parent = Node(position=GRID_POS);

	# Parameters to pass to the creation of ShapeNode
	params = {
		"path": Path.rect(0, 0, GRID_SIZE, GRID_SIZE * ROWS),
		"fill_color": "clear",
		"stroke_color": "lightgrey"
	}
	
	# Building the columns
	for i in range(COLUMNS):
		n = ShapeNode(**params)
		pos = Vector2(i*GRID_SIZE, 0)
		n.position = pos
		n.anchor_point = Vector2(0,0)
		parent.add_child(n)
	
	return parent

class TetrisGame (Scene):
	"""
	The main game code for Tetris
	"""
	def setup(self):
		self.background_color = COLORS["bg"]
		self.game_field = Node(parent=self);
		
		# Add the background grid
		self.bg_grid = build_background_grid()
		self.game_field.add_child(self.bg_grid)
	
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
	run(TetrisGame(), PORTRAIT, show_fps=True) 
