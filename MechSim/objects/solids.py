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

	def setPoint(self):
		self.A = [((self.pos[0] - self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] - self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] - self.dim[2]/2) * math.cos(self.posR[2]))]
		self.B = [((self.pos[0] + self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] - self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] - self.dim[2]/2) * math.cos(self.posR[2]))]
		self.C = [((self.pos[0] - self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] + self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] - self.dim[2]/2) * math.cos(self.posR[2]))]
		self.D = [((self.pos[0] + self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] + self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] - self.dim[2]/2) * math.cos(self.posR[2]))]
		self.E = [((self.pos[0] - self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] - self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] + self.dim[2]/2) * math.cos(self.posR[2]))]
		self.F = [((self.pos[0] + self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] - self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] + self.dim[2]/2) * math.cos(self.posR[2]))]
		self.G = [((self.pos[0] - self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] + self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] + self.dim[2]/2) * math.cos(self.posR[2]))]
		self.H = [((self.pos[0] + self.dim[0]/2) * math.cos(self.posR[0])), ((self.pos[1] + self.dim[1]/2) * math.cos(self.posR[1])), ((self.pos[2] + self.dim[2]/2) * math.cos(self.posR[2]))]

	def quickCollision(self, quickCollisionXDimB, quickCollisionYDimB, quickCollisionZDimB):
		collision = False
		if self.quickCollisionXDim[0] < quickCollisionXDimB[1] and self.quickCollisionXDim[1] > quickCollisionXDimB[0]:
			if self.quickCollisionYDim[0] < quickCollisionYDimB[1] and self.quickCollisionYDim[1] > quickCollisionYDimB[0]:
				if self.quickCollisionZDim[0] < quickCollisionZDim[1] and self.quickCollisionZDim[1] > quickCollisionZDimB[0]:
					collision = True
				else:
					pass
			else:
				pass
		else:
			pass
		return collision

	def redefineQuickCollisionBoundingBox(self):
		setPoint()
		self.xPointArray = [self.A[0], self.B[0], self.C[0], self.D[0], self.E[0], self.F[0], self.G[0], self.H[0]]
		self.xPointArray.sort()
		self.yPointArray = [self.A[1], self.B[1], self.C[1], self.D[1], self.E[1], self.F[1], self.G[1], self.H[1]]
		self.yPointArray.sort()
		self.zPointArray = [self.A[2], self.B[2], self.C[2], self.D[2], self.E[2], self.F[2], self.G[2], self.H[2]]
		self.zPointArray.sort()
		self.quickCollisionXDim = [self.xPointArray[0], self.xPointArray[7]]
		self.quickCollisionYDim = [self.yPointArray[0], self.yPointArray[7]]
		self.quickCollisionZDim = [self.zPointArray[0], self.zPointArray[7]]