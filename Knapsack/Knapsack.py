class TooHeavyException(Exception):
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)
		
class Knapsack():
	def __init__(self, capacity, items = [], current = 0, value = 0):
		self.items = items
		self.capacity = capacity
		self.current = current
		self.value = value
	def addItem(self, item):
		if self.capacity >= self.current + item.weight:
			self.items.append(item)
			self.current += item.weight
			self.value += item.value
		else:
			raise TooHeavyException("Item too heavy!")
	def removeItem(self, item):
		self.items.remove(item)
		self.current -= item.weight
		self.value -= item.value
	def getMinWeight(self):
		return sorted(self.items, key = lambda x: x.weight)[0]
	def addFractionalItem(self, item):
		self.items.append(item)
		capLeft = self.capacity - self.current
		self.current += capLeft
		self.value += item.valuePerUnitWeight * capLeft
	def hasSpace(self):
		return self.current < self.capacity
	def getSpace(self):
		return self.capacity - self.current 
	def copy(self):
		return Knapsack(self.capacity, self.items, self.current, self.value)
		
	
class Item():
	def __init__(self, line):
		line = line.split(" ")
		self.id = int(line[0])
		self.value = int(line[1])
		self.weight = int(line[2])
		self.valuePerUnitWeight = self.value / float(self.weight)
		
	def __str__(self):
		return "{}, {}, {}".format(self.id, self.value, self.weight)
		
class FractionalKnapsackProblem():
	def __init__(self, file, items = [], knapsack = []):
		self.currMax = 0
		self.items = items
		self.knapsack = knapsack
		if self.knapsack == []:
			f = open(file).readlines()
			self.knapsack = Knapsack(int(f[0]))
			for line in f[1:]:
				self.items.append(Item(line))
			
	def evaluate(self, solution):
		for value in solution:
			try:
				self.knapsack.addItem(self.items[int(value)])
			except TooHeavyException:
				self.knapsack.addFractionalItem(self.items[int(value)])
				return self.knapsack.value
				
	def greedyEval(self):
		self.items.sort(key=lambda x: x.valuePerUnitWeight)
		self.items = self.items[::-1]
		for item in self.items:
			try:
				self.knapsack.addItem(item)
			except TooHeavyException:
				self.knapsack.addFractionalItem(item)
				return self.knapsack.value

class ZeroOneKnapsackProblem(FractionalKnapsackProblem):
	def evaluate(self, solution):
		for value in solution:
			try:
				self.knapsack.addItem(self.items[int(value)])
			except TooHeavyException:
				return self.knapsack.value
				
		
if __name__ == "__main__":
	#frkp = FractionalKnapsackProblem("test")
	#print frkp.greedyEval()
	zokp = ZeroOneKnapsackProblem("test")