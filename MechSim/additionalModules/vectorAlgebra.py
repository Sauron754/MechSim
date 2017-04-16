def add2(vectorA, vectorB):
	vectorOut = [vectorA[0] + vectorB[0], vectorA[1] + vectorA[1]]
	return vectorOut

def add(vectorA, vectorB):
	vectorOut = [vectorA[0] + vectorB[0], vectorA[1] + vectorB[1], vectorA[2] + vectorB[2]]
	return vectorOut

def scalarProduct2(vectorA, vectorB):
	scalarProductOut = vectorA[0] * vectorB[0] + vectorA[1] * vectorB[1]
	return scalarProductOut

def scalarProduct(vectorA, vectorB):
	scalarProductOut = vectorA[0] * vectorB[0] + vectorA[1] * vectorB[1] + vectorA[2] * vectorB[2]
	return scalarProductOut

def length2(vector):
	length = sqrt(vector[0] + vector[1])
	return length

def length(vector):
	length = sqrt(vector[0] + vector[1] + vector[2])
	return length

def angle2(vectorA, vectorB):
	phi = math.acos(scalarProduct2(vectorA, vectorB) / length2(vectorA, vectorB))
	return phi

def angle(vectorA, vectorB):
	phi = math.acos(scalarProduct(vectorA, vectorB) / lenght(vectorA, vectorB))
	return phi

def vectorScalarProduct2(vector, scalar):
	vectorOut = [vector[0] * scalar, vector[1] * scalar]
	return vectorOut

def vectorScalarProduct(vector, scalar):
	vectorOut = [vector[0] * scalar, vector[1] * scalar, vector[2] * scalar]
	return vectorOut

def crossProduct(vectorA, vectorB):
	vectorOut = [(vectorA[1] * vectorB[2] - vectorA[2] * vectorB[1]), (vectorA[2] * vectorB[0] - vectorA[0] * vectorB[2]), (vectorA[0] * vectorB[1] - vectorA[1] * vectorB[0])]
	return vectorOut
