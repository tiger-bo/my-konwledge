#!/usr/bin/python3
import draw
import select, evdev, logging

KEY_UP = 103
KEY_DOWN = 108
KEY_LEFT = 105
KEY_RIGHT = 106

class Gui_2048(object):
	"""docstring for Gui_2048"""
	
	def __init__(self, p_x = 0, p_y = 0, x = 4, y = 4):
		super(Gui_2048, self).__init__()
		self.pos_x = p_x
		self.pos_y = p_y
		self.size_x = x
		self.size_y = y
		self.my2048 = []

		for x in range(0, self.size_x):
			for y in range(0, self.size_y):
				bb = draw.box(p_x = x * 10 + self.pos_x, p_y = y * 6 + self.pos_y)
				self.my2048.append(bb)
				bb.insert_to_draw()
	def draw(self):		
		draw.Draw()
	def set_value(self, p_x, p_y, val):
		self.my2048[p_y * self.size_x + p_x].add_info(val)
		self.my2048[p_y * self.size_x + p_x].insert_to_draw()

	def up_active(self):
		pushflag = 0
		for j in range(0, self.size_y):
			pass

def main():
	gg = Gui_2048(77,20)


def test():

	log = logging.FileHandler("2048.log")
	log.setLevel(logging.INFO)
	gg = Gui_2048(77,20)
	index = 0
	for y in range(0,4):
		for x in range(0,4):
			gg.set_value(y, x, index)
			index += 1

	gg.draw()

	dev = evdev.InputDevice('/dev/input/event4')

	log.info(str(dev))
	while True:
	    select.select([dev],[],[])
	    for event in dev.read():
	        if(event.value == 1 or event.value == 0) and event.code != 0:
	            if event.code == KEY_UP:
	            	log.info("KEY_UP\n")
	            elif event.code == KEY_DOWN:
	            	log.info("KEY_DOWN\n")
	            elif event.code == KEY_LEFT:
	            	log.info("KEY_LEFT\n")
	            elif event.code == KEY_RIGHT:
	            	log.info("KEY_RIGHT\n")
	            else:
	            	log.info("else\n")
	log.close()

test()