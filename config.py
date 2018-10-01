from scene import Vector2, get_screen_size

COLUMNS = 10
ROWS = 20

GRID_POS = Vector2(10, 150);
GRID_SIZE= 20;

COLORS = {
	"bg": "#232323",
	"red": "#FF5555",
	"grey": "#646473",
	"blue": "#786CF5",
	"orange": "#FF8C32",
	"green": "#327834",
	"lime": "#92CA49",
	"purple": "#bc36ff",
	"cyan": "#a1ffff",
	"yellow": "#ffff00"
}

UI = {
	"LEFT_BTN": {
		"texture": 'typw:Left',
		"position": Vector2(50, 100)
	},
	"RIGHT_BTN": {
		"texture": 'typw:Right',
		"position": Vector2(150, 100)
	}
}

PIECES = [
	(COLORS["cyan"], (3, ROWS), (4, ROWS), (5, ROWS), (6, ROWS)),
	(COLORS["yellow"], (4, ROWS), (5, ROWS), (4, ROWS-1), (5, ROWS-1)),
	(COLORS["purple"], (4, ROWS), (3, ROWS-1), (4, ROWS-1), (5, ROWS-1))
]

INITIAL_FALL_SPEED = 1
LOCK_DELAY = 0.5
