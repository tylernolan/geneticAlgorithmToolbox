from TSP import TravellingSalesman
from Knapsack import Knapsack
from GeneticAlgorithm import GeneticAlgorithm
from SolutionFactory import SolutionFactory
from Gene import *
from TSP import TravellingSalesman
import operator
from pympler import muppy
from pympler import summary
import types
import gc
import objgraph
'''
Structure for comparing genetic algorithm candidates, holds the maximum value found in the run, and the generation where that value was found.
'''
class GA_Opt_Struct():
	def __init__(self, maximum, maxFound, solution):
		self.maximum = maximum
		self.maxFound = maxFound
		self.solution = solution
	'''
	If it finds a greater max than the previous, return it was greater. If they find the same max value, the one that found it faster is better.
	'''
	def __cmp__(self, other):
		if self.maximum > other.maximum:
			return 1
		elif self.maximum == other.maximum:
			if self.maxFound > other.maxFound:
				return 1
			elif self.maxFound == other.maxFound:
				return 0
			elif self.maxFound < other.maxFound:
				return -1
		elif self.maximum < other.maximum:
			return -1
	
	def __str__(self):
		return "Max: {}, \nFound at Generation: {}\n\n {}".format(self.maximum, self.maxFound, self.solution)

'''
Class that holds a variety of sample fitness functions.
'''
class FitnessFunctions():		
	'''
	Returns an optimized GA for a given problem
	'''
	@staticmethod
	def GAOptimizer(solution):
		mutationChance = solution["mutationChance"].value
		numParents = solution["numParents"].value
		selectionThreshold = solution["selectionThreshold"].value
		percentRandom = solution["percentRandom"].value
		filename = solution["file"].value
		alg = solution["func"].value
		sf = SolutionFactory()
		
		for i in range(50):
			sf.addGene(str(i),0,1, geneType = Gene)
		sf.addGene("file", filename, geneType = ConstGene)
		ga = GeneticAlgorithm(sf, alg, numGenerations=20, generationSize = 30, mutationChance = mutationChance, numParents = numParents, selectionThreshold = selectionThreshold, percentRandom = percentRandom)#, extraTerminationCondition = etc)
		
		genMaxFound = ga.genMaxFound
		maximum = ga.getMax()
		return GA_Opt_Struct(maximum, genMaxFound, solution)
		
	'''
	Fitness Function for the Travelling Salesman Problem.
	File it tests is located in the TSP folder, config2.txt.
	'''
	@staticmethod
	def travellingSalesmanFunction(solution):
		#To get exclusivity, sort the keys of the GeneticRepresentation by their value and use those, rather than the values directly.
		sortedKeys = sorted(solution.keys(), key=lambda x: solution[x].value)
		valList = [int(x) for x in sortedKeys]
		tsp = TravellingSalesman.TravellingSalesmanProblem()
		#return a negative because we want to minimize the function.
		return -(tsp.runTrial(valList))
		#return solution["479"].value
		#return sum([x.value for x in solution.values()])
	
	'''
	Fitness function for a solution for the fractional knapsack problem in file "test"
	Both this method and the following methods can trivally be optimized to not need to read from a file each time by having only a single instance of the frkp/zokp object.
	'''	
	@staticmethod
	def fractionalKnapsack(solution):
		solution = dict(solution)
		file = solution["file"].value
		del solution["file"]
		
		sortedKeys = sorted(solution.keys(), key=lambda x: solution[x].value)
		valList = [int(x) for x in sortedKeys]
		frkp = Knapsack.FractionalKnapsackProblem(str(file))
		return frkp.evaluate(valList)
		
	'''
	Fitness function for a solution to the zero-one knapsack problem located in the file "test"
	'''	
	@staticmethod
	def zeroOneKnapsack(solution):
		sortedKeys = sorted(solution.keys(), key=lambda x: solution[x].value)
		valList = [int(x) for x in sortedKeys]
		zokp = Knapsack.ZeroOneKnapsackProblem("test")
		return zokp.evaluate(valList)	
		
	'''
	Very simple function to demonstrate the functionality of the library. Seeks to maximize 1, 2, and 3, while minimizing 4.
	'''
	@staticmethod
	def simpleFitnessFunction(solution):
		return ((solution["1"].value * solution["2"].value) + solution["3"].value) / (solution["4"].value)