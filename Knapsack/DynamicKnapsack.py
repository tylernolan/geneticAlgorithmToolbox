from Knapsack import *
class DynamicKnapsack(FractionalKnapsackProblem):
	def evaluate(self):
		#fill the table with default values so we can easily manipulate the 2d list.
		self.table = []
		for i in range(len(self.items)):
			self.table.append([0 for x in range(self.knapsack.capacity+1)])
			
		#self.items.sort(key = lambda x: x.valuePerUnitWeight)
		for g in range(self.knapsack.capacity+1):
			for i in range(len(self.items)):
				item = self.items[i]
				#the basic operation is safe
				if g - item.weight >= 0 and i - 1 >= 0: 
					if (self.table[i-1][g-item.weight] + item.value) > self.table[i-1][g]:
						self.table[i][g] = self.table[i-1][g-item.weight] + item.value
					else:
						self.table[i][g] = self.table[i-1][g]
				#accessing g -iw is unsafe, but there is a row above.
				elif g - item.weight < 0 and i - 1 >= 0: 
					self.table[i][g] = self.table[i-1][g]
				#there is no row above	
				else:
					if item.weight > g:
						self.table[i][g] = 0
					else:
						self.table[i][g] = item.value
						
	def tableToCSV(self, filename="out.csv"):
		outStr = "Weights, "
		for i in range(len(self.table[0])):
			outStr += "{},".format(i)
		outStr += "\n"
		for row in range(len(self.table)):
				outStr += "Item {}, ".format(row)
				for item in range(len(self.table[row])):
					outStr += "{},".format(self.table[row][item])
				outStr += "\n"
		file = open(filename, 'w')
		file.write(outStr)
		file.close()
		
	def getMax(self):
		return self.table[len(self.table)-1][len(self.table[1])-1]
		
if __name__ == "__main__":
	dk = DynamicKnapsack("test")
	dk.evaluate()
	print dk.getMax()
	dk.tableToCSV()