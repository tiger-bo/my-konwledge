#!/usr/bin/python3


#突然发现Python的class还没看

class box(object):
	"""docstring for box"""
	def __init__(self, x = 11, y = 6, value = 0):
		super(box, self).__init__()
		self.size_x = x
		self.size_y = y
		self.box_vl	= value

	def setvalue(self,value):
		self.box_vl = value

	def drawbox(self):
		for y in range(0, self.size_y + 1) :
			for x in range(0, self.size_x + 1):
				if y in [0, self.size_y]:
					print("-",end='')
				elif y == self.size_y / 2:
					print("-",end='')
				else:
					if x in [0, self.size_x]:
						print("|",end='')
					else:
						print(" ",end='')
			print()	

x = box()
x.drawbox()
