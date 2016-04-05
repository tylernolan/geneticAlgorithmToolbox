from Knapsack import *
class DynamicKnapsack(FractionalKnapsackProblem)
	def evaluate(self):
		table = []
		for i in range(len(self.items)):
			table.append([0 for x in range(self.knapsack.capacity+1)])
		self.items.sort(key = lambda x: x.valuePerUnitWeight)
		for i in range(self.knapsack.capacity+1):
			for g in range(self.items+1):
				item = self.items[g]
				if g-item.weight >= 0 and i-1 >= 0:
					if table[i-1][g-item.weight] + item.weight:
						table[i][g] = table[i-1][g-item.weight] + item.weight
					else:
						table[i][g] = table[i-1][g]
					
					
				except IndexError:
					