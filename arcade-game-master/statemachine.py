#WIP
class FSM:
	def __init__(self):
		self.activeState = None

	def set_state(self, state):
		self.activeState = state

	def update(self):
		if self.activeState != None:
			self.activeState()