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
		self.posR = posR
		self.dim = dim
		self.motT = motT
		self.motR = motR
		setPoint(pos, posR, dim)
		#this determines which of the points is the most far out
		self.xPointArray = [self.A[0], self.B[0], self.C[0], self.D[0], self.E[0], self.F[0], self.G[0], self.H[0]]
		self.xPointArray.sort()
		self.yPointArray = [self.A[1], self.B[1], self.C[1], self.D[1], self.E[1], self.F[1], self.G[1], self.H[1]]
		self.yPointArray.sort()
		self.zPointArray = [self.A[2], self.B[2], self.C[2], self.D[2], self.E[2], self.F[2], self.G[2], self.H[2]]
		self.zPointArray.sort()
		self.quickCollisionXDim = [self.xPointArray[0], self.xPointArray[7]]
		self.quickCollisionYDim = [self.yPointArray[0], self.yPointArray[7]]
		self.quickCollisionZDim = [self.zPointArray[0], self.zPointArray[7]]

	def setPoint(self, pos, posR, dim):
		self.A = [((pos[0] - dim[0]/2) * math.cos(posR[0])), ((pos[1] - dim[1]/2) * math.cos(posR[1])), ((pos[2] - dim[2]/2) * math.cos(posR[2]))]
		self.B = [((pos[0] + dim[0]/2) * math.cos(posR[0])), ((pos[1] - dim[1]/2) * math.cos(posR[1])), ((pos[2] - dim[2]/2) * math.cos(posR[2]))]
		self.C = [((pos[0] - dim[0]/2) * maht.cos(posR[0])), ((pos[1] + dim[1]/2) * math.cos(posR[1])), ((pos[2] - dim[2]/2) * math.cos(posR[2]))]
		self.D = [((pos[0] + dim[0]/2) * maht.cos(posR[0])), ((pos[1] + dim[1]/2) * math.cos(posR[1])), ((pos[2] - dim[2]/2) * math.cos(posR[2]))]
		self.E = [((pos[0] - dim[0]/2) * maht.cos(posR[0])), ((pos[1] - dim[1]/2) * math.cos(posR[1])), ((pos[2] + dim[2]/2) * math.cos(posR[2]))]
		self.F = [((pos[0] + dim[0]/2) * maht.cos(posR[0])), ((pos[1] - dim[1]/2) * math.cos(posR[1])), ((pos[2] + dim[2]/2) * math.cos(posR[2]))]
		self.G = [((pos[0] - dim[0]/2) * maht.cos(posR[0])), ((pos[1] + dim[1]/2) * math.cos(posR[1])), ((pos[2] + dim[2]/2) * math.cos(posR[2]))]
		self.H = [((pos[0] + dim[0]/2) * maht.cos(posR[0])), ((pos[1] + dim[1]/2) * math.cos(posR[1])), ((pos[2] + dim[2]/2) * math.cos(posR[2]))]

	def quickCollision(self, point):
		collision = False
		if point[0] > self.quickCollisionXDim[0] and point[0] < self.quickCollisionXDim[1]:
			if point[1] > self.quickCollisionYDim[0] and point[1] < self.quickCollisionYDim[1]:
				if point[2] > self.quickCollisionZDim[0] and point[2] < self.quickCollisionZDim[1]:
					collision = True
				else:
					collision = False
			else:
				pass
		else:
			pass
