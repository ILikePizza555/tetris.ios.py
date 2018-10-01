from config import *
from scene import *
from ui import Path
import sound
import random
import math
A = Action


def clamp(x, minimum, maximum):
	return max(minimum, min(x, maximum))


def intersects_sprite(point, sprite):
	norm_pos = Vector2()
	norm_pos.x = sprite.position.x - (sprite.size.w * sprite.anchor_point.x)
	norm_pos.y = sprite.position.y - (sprite.size.h * sprite.anchor_point.y)
	
	return (point.x >= norm_pos.x and point.x <= norm_pos.x + sprite.size.w) and (point.y >= norm_pos.y and point.y <= norm_pos.y + sprite.size.h)


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
		if col < 0:
			raise ValueError(f"col={col} is less than 0")
		
		if row < 0:
			raise 
			ValueError(f"row={row} is less than 0")
		
		self.col = col
		self.row = row
		
		pos = Vector2()
		pos.x = col * self.size.w
		pos.y = row * self.size.h
		self.position = pos
		

class PieceControl ():
	"""
	An object that controls a group of tiles.
	"""
	def __init__(self, tiles=[]):
		"""
		Constructs a new PieceControl.
		
		Parameters:
			tiles: A list of Tile objects under the control of this object.
		"""
		self.tiles = tiles

	def reset(self, tiles=[]):
		self.tiles = tiles
	
	def rotate(self):
		pass
	
	def move(self, d_col=0, d_row=0):
		for t in self.tiles:
			col = clamp(t.col + d_col, 0, COLUMNS - 1)
			row = clamp(t.row + d_row, 0, ROWS - 1)
			t.set_pos(col, row)

class TetrisGame(Scene):
	"""
	The main game code for Tetris
	"""
	def setup_ui(self):
		# Root node for UI elements
		self.ui_root = Node(parent=self)
		
		self.left_btn = SpriteNode(**UI["LEFT_BTN"], parent=self.ui_root)
		
		self.right_btn = SpriteNode(**UI["RIGHT_BTN"],parent=self.ui_root)
	
	def setup(self):
		self.background_color = COLORS["bg"]
		
		# Root node for all game elements
		self.game_field = Node(parent=self, position=GRID_POS)
		
		# Add the background grid
		self.bg_grid = build_background_grid()
		self.game_field.add_child(self.bg_grid)
		
		self.drop_timer = INITIAL_FALL_SPEED
		
		self.control = PieceControl([])
		self.spawn_piece()
		
		self.setup_ui()
		
	def get_tiles(self, exclude=[]):
		"""
		Returns an iterator over all tile objects
		"""
		for o in self.game_field.children:
			if isinstance(o, Tile) and o not in exclude:
				yield o
				
	def check_control_row_collision(self):
		"""
		Returns true if any of the tiles in self.control row-collide (is row-adjacent) with the tiles on the field
		"""
		for t in self.control.tiles:
			if t.row == 0:
				return True
			
			for gt in self.get_tiles(exclude=self.control.tiles):
				if t.row == gt.row + 1 and t.col == gt.col:
					return True
				
		return False
		
	def check_left_collision(self):
		"""
		Checks the left side of the control piece for collision
		"""
		for t in self.control.tiles:
			if t.col == 0:
				return True
		
			for gt in self.get_tiles(exclude=self.control.tiles):
				if t.col == gt.col + 1 and t.row == gt.row:
					return True
		
		return False
		
	def check_right_collision(self):
		"""
		Check the right side of the control piece for collision
		"""
		for t in self.control.tiles:
			if t.col == COLUMNS - 1:
				return True
			
			for gt in self.get_tiles(exclude=self.control.tiles):
				if t.col == gt.col - 1 and t.row == gt.row:
					return True
			
		return False
		
	def spawn_piece(self):
		"""
		Spawns a new piece on the game field and adds it to self.control
		"""
		template = random.choice(PIECES)
		color = template[0]
		positions = template[1:]
		
		tiles = []
		for p in positions:
			t = Tile(color, *p)
			self.game_field.add_child(t)
			tiles.append(t)
		
		self.control.reset(tiles)
	
	def did_change_size(self):
		pass
	
	def update(self):
		self.drop_timer -= self.dt
		if self.drop_timer <= 0:
			self.control.move(d_row=-1)
			self.drop_timer = INITIAL_FALL_SPEED
			
			# Check for intersection and spawn a new piece if needed
			if self.check_control_row_collision():
				self.spawn_piece()
	
	def touch_began(self, touch):
		if intersects_sprite(touch.location, self.left_btn) and not self.check_left_collision():
			self.control.move(-1)
		elif intersects_sprite(touch.location, self.right_btn) and not self.check_right_collision():
			self.control.move(1)
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(TetrisGame(), PORTRAIT, show_fps=True) 
