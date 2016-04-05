import random
from GeneticRepresentation import GeneticRepresentation
from collections import defaultdict
'''
This is where the user input comes from, genetic representations are built here.
'''
class SolutionFactory():
	def __init__(self):
		self.genome = []
		
	#geneType kwarg is Gene class you want to use as a blueprint for the gene.
	#args are the arguments for the gene's constructor in order.
	def addGene(self, *args, **kwargs):
		geneType = (kwargs["geneType"])
		args = list(args)
		args.append(geneType)
		self.genome.append(args)
		
	#combines a number of parents into a new genetic representation.
	def combine(self, parents):
		newSolution = GeneticRepresentation()
		genes = parents[0].keys()
		for gene in genes:
			randParent = random.choice(parents)
			newSolution[gene] = randParent[gene].copy()
		return newSolution

	def generateRandomSolution(self):
		solution = GeneticRepresentation()
		for gene in self.genome:
			#last item in the gene list is the geneType, the first is the dictionary key. Middle arguments are splatted into the Gene constructor.
			solution[gene[0]] = gene[-1](*gene[1:-1])
		return solution

	def initializeGeneration(self, size):
		ret = []
		for i in range(size):
			ret.append(self.generateRandomSolution())
		return ret