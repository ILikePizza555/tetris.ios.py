from config import *
from scene import *
from ui import Path
import sound
import random
import math
A = Action

def build_background_grid():
	parent = Node();

	# Parameters to pass to the creation of ShapeNode
	params = {
		"path": Path.rect(0, 0, GRID_SIZE, GRID_SIZE * ROWS),
		"fill_color": "clear",
		"stroke_color": "lightgrey"
	}
	
	anchor = Vector2(0, 0)
	
	# Building the columns
	for i in range(COLUMNS):
		n = ShapeNode(**params)
		pos = Vector2(i*GRID_SIZE, 0)
		
		n.position = pos
		n.anchor_point = anchor
		
		parent.add_child(n)
	
	# Building the rows
	params["path"] = Path.rect(0, 0, GRID_SIZE * COLUMNS, GRID_SIZE)
	for i in range(ROWS):
		n = ShapeNode(**params)
		pos = Vector2(0, i*GRID_SIZE)
		
		n.position = pos
		n.anchor_point = anchor
		
		parent.add_child(n)
		
	return parent


class Tile(SpriteNode):
	"""
	A single tile on the grid.
	"""
	def __init__(self, color, col=0, row=0):
		SpriteNode.__init__(self, 'pzl:Gray3')
		self.color = color
		self.size = (GRID_SIZE, GRID_SIZE)
		self.anchor_point = (0, 0)
		self.set_pos(col, row)
	
	def set_pos(self, col=0, row=0):
		"""
		Sets the position of the tile in the grid.
		"""
		if col >= COLUMNS:
			raise ValueError(f"col={col} is larger than COLUMNS={COLUMNS}")
		
		if row >= ROWS:
			raise 
			ValueError(f"row={row} is larger than ROWS={ROWS}")
		
		pos = Vector2()
		pos.x = col * self.size.w
		pos.y = row * self.size.h
		self.position = pos
		

class TetrisGame(Scene):
	"""
	The main game code for Tetris
	"""
	def setup(self):
		self.background_color = COLORS["bg"]
		
		# Root node for all game elements
		self.game_field = Node(parent=self, position=GRID_POS)
		
		# Add the background grid
		self.bg_grid = build_background_grid()
		self.game_field.add_child(self.bg_grid)
		
		# Root node for UI elements
		self.ui_root = Node(parent=self)
		
		self.left_btn = SpriteNode(**UI["LEFT_BTN"], parent=self.ui_root)
		
		self.right_btn = SpriteNode(**UI["RIGHT_BTN"],parent=self.ui_root)
	
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
