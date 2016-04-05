from collections import defaultdict
class TravellingSalesmanProblem():
	def __init__(self):
		self.file = open("config2.txt", 'r').readlines()
		self.locationList = []
		for line in self.file:
			self.locationList.append(Location(line.split(",")))
			
	def runTrial(self, inputs):
		self.salesman = Salesman(self.locationList, inputs[0])
		for input in inputs[1:]:
			self.salesman.travel(input)
		return self.salesman.distanceTravelled
class Location():
	def __init__(self, args):
		self.locDict = defaultdict(int)
		for i in range(len(args)):
			self.locDict[i] = args[i].strip()
			
def AlreadyVisitedException(Exception):
	pass
class Salesman():
	def __init__(self, locationList, startingLoc):
		self.visited = [startingLoc]
		self.current = startingLoc
		self.locationList = locationList
		self.distanceTravelled = 0
		
	def travel(self, destination):
		if destination in self.visited:
			self.travel((destination + 1)%len(self.locationList))
		else:
			self.distanceTravelled += int(self.locationList[self.current].locDict[destination])
			self.current = destination
			self.visited.append(destination)
	