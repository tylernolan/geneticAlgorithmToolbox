import random
'''
This class may require major overhauls for certain applications. Made to be extendable. 
By default, all Genes hold a float value, and have a possible range of float values between a min val and a max val.
'''
class Gene():
	def __init__(self, minVal, maxVal, value = None, randSource = None):
		self.minVal = minVal
		self.maxVal = maxVal
		if randSource == None: randSource = Gene
		if value == None:
			self.value = randSource.generateRandomValue(self)
		else:
			self.value = value

	def generateRandomValue(self):
		return random.uniform(self.minVal, self.maxVal)
	'''
	when extending gene, you must rewrite mutate() and copy() with the appropriate constructors.
	'''
	def mutate(self):
		return Gene(self.minVal, self.maxVal, value=self.generateRandomValue())
		
	'''
	when extending gene, you must rewrite mutate() and copy() with the appropriate constructors.
	'''
	def copy(self):
		return Gene(self.minVal, self.maxVal, value=self.value)

	def __eq__(self, other):
		return self.value == other.value

	def __repr__(self):
		return str(self.value)

	def __str__(self):
		return str(self.value)
		
'''
Gene to pass constant values, or functions into a genetic representation for use in the fitness function.
Allows for more layers of abstraction.
'''
class ConstGene(Gene):
	def __init__(self, value):
		self.value = value
	def generateRandomValue(self):
		return self.value
	def mutate(self):
		return self
	#ConstGenes should never change after creation, so returning self is equivalent to making a copy. 
	def copy(self):
		return self
'''
This gene takes an extra parameter for the range which it can mutate
if rangeChange is 1, then it will only change + or - 1 value when mutating
ex. if it's value is 8, and rangeChange is 1 and it mutates, it will only mutate to 7, 8, or 9.
'''
class CMGene(Gene):
	def __init__(self, rangeChange, minVal, maxVal, value = None, randSource=None):
		Gene.__init__(self, minVal, maxVal, value=value)
		self.rangeChange = rangeChange

	def generateRandomValue(self):
		minimum = self.minVal
		maximum = self.maxVal
		if self.value-self.rangeChange > self.minVal:
			minimum = self.value - self.rangeChange
		if self.value + self.rangeChange < self.maxVal:
			maximum = self.value + self.rangeChange
		return random.uniform(minimum, maximum)
	def mutate(self):
		return CMGene(self.rangeChange, self.minVal, self.maxVal, value=self.generateRandomValue())

	def copy(self):
		return CMGene(self.rangeChange, self.minVal, self.maxVal, value=self.value)
'''
Similar to base gene, but value is always an integer. 
'''
class IntGene(Gene):
	def __init__(self, minVal, maxVal, value = None, randSource = None):
		Gene.__init__(self, minVal, maxVal, value = value, randSource = IntGene)#self.__class__)

	def generateRandomValue(self):
		return random.randint(self.minVal, self.maxVal)

	def mutate(self):
		return IntGene(self.minVal, self.maxVal, value=self.generateRandomValue())

	def copy(self):
		return IntGene(self.minVal, self.maxVal, value=self.value)
'''
the integer version of CMGene
'''
class IntCMGene(IntGene):
	def __init__(self, rangeChange, minVal, maxVal, value=None):
		IntGene.__init__(self, minVal, maxVal, value = value)
		self.rangeChange = rangeChange

	def generateRandomValue(self):
		minimum = self.minVal
		maximum = self.maxVal
		if self.value-self.rangeChange > self.minVal:
			minimum = self.value - self.rangeChange
		if self.value + self.rangeChange < self.maxVal:
			maximum = self.value + self.rangeChange
		ret = random.randint(minimum, maximum)
		return ret

	def mutate(self):
		newGene = IntCMGene(self.rangeChange, self.minVal, self.maxVal, value=self.generateRandomValue())
		return newGene

	def copy(self):
		return IntCMGene(self.rangeChange, self.minVal, self.maxVal, value=self.value)
