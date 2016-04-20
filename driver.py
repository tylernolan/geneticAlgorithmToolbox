from GeneticAlgorithm import GeneticAlgorithm
from SolutionFactory import SolutionFactory
from Gene import *
from TSP import TravellingSalesman
import operator
from FitnessFunctions import FitnessFunctions
import time

'''
Sample extra termination condition
'''
def etc(currMax):
	if fitnessFunction(currMax) > 105:
		return True

'''
Function to build a solution factory for genetic algorithm parameters. 
'''
def GeneticAlgorithmSolutionFactoryBuilder():
	gasf = SolutionFactory()
	gasf.addGene("mutationChance",.05, 0, 1, geneType = CMGene)
	gasf.addGene("numParents",2, 2, 10, geneType = IntCMGene)
	gasf.addGene("selectionThreshold", .05, 0, 1, geneType = CMGene)
	gasf.addGene("percentRandom", .05, 0, 1, geneType = CMGene)
	gasf.addGene("file", "test", geneType = ConstGene)
	gasf.addGene("func", FitnessFunctions.fractionalKnapsack, geneType = ConstGene)
	return gasf

if __name__ == "__main__":
	file = open("log.txt", 'w')
	file.close()
	sf = SolutionFactory()
	#factory for optimizing the GA
	#build the genome
	#call addGene in the same order you'd call your Gene constructor.
	#default Genes have the following argument order: dictKey, minValue, maxValue.
	#ControlledMutationGenes(CMGene, IntCMGene) have an additional argument inbetween dictKey and minValue for the range a mutation can mutate.
	#ConstGene has just key, val, and geneType arguments fac.addGene("file", "test.txt", geneType = ConstGene)
	for i in range(50):
		sf.addGene(str(i),0,1, geneType = Gene)
	sf.addGene("file", "test", geneType = ConstGene)
	
	gasf = GeneticAlgorithmSolutionFactoryBuilder()
	s = time.time()
	ga = GeneticAlgorithm(gasf, FitnessFunctions.GAOptimizer, numGenerations=50, generationSize = 16)#, extraTerminationCondition = etc)
	#ga = GeneticAlgorithm(sf, FitnessFunctions.fractionalKnapsack, numGenerations=50, generationSize=50)
	print time.time() - s
	print ga.getLastGeneration()
	print ga.getMax()
	#print FitnessFunctions.fractionalKnapsack(ga.getMax())
	#print ga.genMaxFound
