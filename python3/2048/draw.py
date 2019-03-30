#!/usr/bin/python3


import os

Draw_X = os.get_terminal_size().columns
Draw_Y = os.get_terminal_size().lines

Draw_buf = [' ' for x in range(0, Draw_X*Draw_Y)]


def Draw():
	for p in Draw_buf:
		print(p,end='')
	print()

def Clean():
	for x in range(0, Draw_X*Draw_Y):
		Draw_buf[x] = ' '
def main():
	pass

class point(object):
	"""docstring for point"""
	def __init__(self, x = 0, y = 0, c = '*'):
		super(point, self).__init__()
		self.pos_x = x
		self.pos_y = y
		self.ch = c

	def insert_to_draw(self):
		if self.pos_y >= Draw_Y | self.pos_x >= Draw_X:
			pass
		else:
			Draw_buf[Draw_X * self.pos_y + self.pos_x] = self.ch



class box(object):
	"""docstring for box"""

	def __init__(self, p_x = 0, p_y = 0, x = 11, y = 7, inf = ''):
		super(box, self).__init__()
		self.box_x = x
		self.box_y = y
		self.pos_x = p_x
		self.pos_y = p_y
		self.info = inf
		self.box_buf = [' ' for x in range(0, self.box_x * self.box_y)]
		for y in range(0, self.box_y):
			for x in range(0, self.box_x):
				if y in [0, self.box_y - 1]:
					self.box_buf[y * self.box_x + x] = '-'
				else:
					if x in [0, self.box_x - 1]:
						self.box_buf[y * self.box_x + x] = '|' 


	def insert_to_draw(self):
		for y in range(0, self.box_y ) :
			for x in range(0, self.box_x ):
				Draw_buf[(y + self.pos_y) * Draw_X + self.pos_x + x] = self.box_buf[y * self.box_x + x]

	def add_info(self, value):
		strval = str(value)
		strlen = len(strval)
		infosize = (self.box_x - 1) * (self.box_y - 1)
		if strlen < infosize:
			index = 0
			for s in strval:
				self.box_buf[int(self.box_x * self.box_y / 2 - strlen / 2 + index)] = s
				index += 1


if __name__ == '__main__':
	main()