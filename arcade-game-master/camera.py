import arcade
from constants import *

class Camera:
	def __init__(self, width, height, target):
		self.width = width
		self.height = height
		self.target = target
		self.targetpos_x = None
		self.targetpos_y = None

	def camera_update(self):
		current_targetpos_x = self.target.center_x
		current_targetpos_y = self.target.center_y
		if (self.targetpos_x, self.targetpos_y) != (current_targetpos_x, current_targetpos_y):
			arcade.set_viewport(current_targetpos_x - (self.width/2),
								current_targetpos_x + (self.width/2),
								current_targetpos_y - (self.height/2),
								current_targetpos_y + (self.height/2))
			self.targetpos_x = current_targetpos_x
			self.targetpos_y = current_targetpos_y
