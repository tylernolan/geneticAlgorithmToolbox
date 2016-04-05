from collections import defaultdict
import random
'''
Genetic representations are dictionaries.
The keys should be descriptive variable names, but can be anything.
The values for this dictionary must always be Genes.

This data structure is used for the main genetic algorithm, as well as the fitness function. 
These can be built via the SolutionFactory class.
'''
class GeneticRepresentation(defaultdict):
	def __init__(self):
		defaultdict.__init__(self, None)
		
	def mutate(self, mutationChance):
		for obj in self.keys():
			if mutationChance > random.random():
				self[obj] = self[obj].mutate()
	def __str__(self):
		ret = ""
		stringSegment = "{} : {}\n"
		for key in self.keys():
			ret += stringSegment.format(key, self[key])
		return ret

	def copy(self):
		cpy = GeneticRepresentation()
		for key in self.keys():
			cpy[key] = self[key].copy()
		return cpy