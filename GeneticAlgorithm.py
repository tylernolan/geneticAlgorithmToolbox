from collections import defaultdict
import random
from SolutionFactory import SolutionFactory
from GeneticRepresentation import GeneticRepresentation
import copy
'''
3 parts needed. 
1. A fitness function, which determines how fit a given solution is.
2. Solutions able to be expressed in atomic parts in a genetic representation. 
3. The high-level "Genetic Representation" which is the basic data structure of the algorithm.

Solution Factory is an object that creates genetic representations.
Generations are lists of genetic representations (solutions)
'''
class GeneticAlgorithm():
	def __init__(self, solutionFactory, fitnessFunction, 
	numGenerations=75, 
	generationSize=80, 
	extraTerminationCondition = None,
	mutationChance = .15,
	numParents = 3,
	selectionThreshold = .2,
	percentRandom = .5
	):
		self.fitnessFunction = fitnessFunction
		self.solutionFactory = solutionFactory
		self.numGenerations = numGenerations
		self.generationSize = generationSize
		self.generations = defaultdict(list)
		self.currGeneration = 0
		self.genMaxFound = 0
		self.mutationChance = mutationChance
		self.numParents = numParents
		self.selectionThreshold = selectionThreshold
		self.percentRandom = percentRandom
		
		self.generations[0] = self.sortGeneration(self.solutionFactory.initializeGeneration(self.generationSize))
		self.currentMax = self.generations[0][-1]
		
		for self.currGeneration in range(self.numGenerations):
			self.nextGeneration(self.currGeneration)
			if extraTerminationCondition != None and extraTerminationCondition(self.currentMax):
				break

	def toCSV(self, filename):
		file = open(filename, 'w')
		for i in range(self.getLastGeneration()+1):
			maxVal = self.getMaximumForGeneration(i)
			file.write("{}|{}\n".format(i, self.fitnessFunction(maxVal)))
		file.close()
		
	def sortGeneration(self, generation):
		return sorted(generation, key=lambda x: self.fitnessFunction(x))
		
	def getMax(self):
		return self.currentMax
	
	def getMaximumForGeneration(self, generation):
		return self.sortGeneration(self.generations[generation])[-1]
		
	def getLastGeneration(self):
		return max(self.generations.keys())
	
	#Performs the base operations of the algorithm
	def nextGeneration(self, i):
		if (self.fitnessFunction(self.getMaximumForGeneration(i))) > (self.fitnessFunction(self.currentMax)):
			#print self.fitnessFunction(self.currentMax)
			#print self.fitnessFunction(self.getMaximumForGeneration(self.currGeneration))
			#print ""
			self.genMaxFound = i
			self.currentMax = self.getMaximumForGeneration(i).copy()
		selectedSolutions = self.select()
		self.mutate(selectedSolutions)
		self.generations[i+1] = self.crossover(selectedSolutions)
		#self.generations[self.currGeneration+1].append(self.currentMax)
	
	#calls the mutate method on each individual solution
	def mutate(self, selectedSolutions):
		for solution in selectedSolutions:
			solution.mutate(self.mutationChance)
			
	def logGeneration(self, generation, genNumber):
		file = open("log.txt", 'a')
		file.write("GENERATION NUMBER {}\n".format(genNumber))
		file.write("GEN MAX = {}\n".format(self.fitnessFunction(generation[-1])))
		for thing in generation:
			file.write(str(self.fitnessFunction(thing))+"\n")
	
	#Fills the next generation with crossover, and new random solutions. 
	def crossover(self, solutionsToCross):
		nextGeneration = []
		parents = []
		nextGeneration.append(self.currentMax.copy())
		for j in range(int(self.generationSize-(self.generationSize*(1-self.percentRandom)))):
			random.shuffle(solutionsToCross)
			parents = solutionsToCross[0:self.numParents]
			nextGeneration.append(self.solutionFactory.combine(parents))
		#fill the rest with new random seedings
		for i in range(self.generationSize - len(nextGeneration)):
			nextGeneration.append(self.solutionFactory.generateRandomSolution())
		nextGeneration = self.sortGeneration(nextGeneration)
		self.logGeneration(nextGeneration, self.currGeneration)
		return nextGeneration
		
	#sort the current generation with the fitness function, return the top threshold% of solutions.
	def select(self):
		#TODO: I could probably significantly cut down the number of copy operations here by only copying the genes I'm returning.
		return [x.copy() for x in self.generations[self.currGeneration][int(-len(self.generations[self.currGeneration])*self.selectionThreshold):]]
		