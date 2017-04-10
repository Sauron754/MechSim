class rectangle():
	"""docstring for rectangle

	quick variable name glossary
	dim = dimension of the vector to the next surface
	pos = position of the calculation point
	posR = state of current rotation (angle between dimension vector and axis)
	max = maximal distance in some direction(this is used to quick check for collisions) 
	motT = translational motion
	motR = rotational motion
	mass = mass
	material = material of the object (irrelevant for now but can be filled out for readability of output)
	"""
	def __init__(self, pos, posR, dim, motT, motR):
				self.pos = pos
				self.dim = dim
				self.motT = motT
				self.motR = motR
				#this determines which of the points is the most far out
				