#!/usr/bin/python
import draw
import asyncio, evdev

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

gg = Gui_2048(77,20)


mouse = evdev.InputDevice('/dev/input/event4')
keybd = evdev.InputDevice('/dev/input/event5')

async def print_events(device):
    async for event in device.async_read_loop():
        print(device.path, evdev.categorize(event), sep=': ')

for device in mouse, keybd:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()