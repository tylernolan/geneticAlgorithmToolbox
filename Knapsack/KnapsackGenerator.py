import random
class KnapsackGenerator():
	def __init__(self, filename, size):
		self.items = []
		self.capacity = "{}\n".format(random.randint(20,90))
		f = open(filename, 'w')
		f.write(self.capacity)
		for i in range(size):
			line = "{} {} {}\n".format(i, random.randint(1,30), random.randint(1,30))
			self.items.append(line)
			f.write(line)
		f.close()
		
if __name__ == "__main__":
	KnapsackGenerator("test", 50)
			