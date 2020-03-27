import client as cl
import random as rand
import numpy as np 
import crossover as cs
import mutation as mut
import selection as sel
key = '4scAFELWNu1oZKJ7xovrpF4uMhuOAtUNizeYl9cAIVx5F8Vp72'

def generate_population():
    new_gen = np.random.uniform(low = -10 , high = 10 , size=(16,11))
    return (new_gen)

def file_input():
    model = open('overfit.txt')
    model = model.read()
    mode = np.fromstring(model.replace("[","").replace("]","",).replace(",","   "),sep="    ")
    model = np.ndarray.tolist(mode)
    return model

def fitness_function(generation):
    fitness = []
    for i in generation:
        fitness_per_individual = cl.get_errors(key,np.ndarray.tolist(i))
        fitness.append(fitness_per_individual)
    return fitness

def main():
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    population = np.load('example.npy')
    while 1:
        fitness = fitness_function(population)
        print(population,fitness)
        np.save('example',population)
        np.save('error',fitness)
        offspring = np.zeros((16,11))
        offspring[0]= sel.roulette_selection(population,fitness)
        offspring[1]= sel.rank_selection(population,fitness)
        parents = np.array([offspring[0],offspring[1]])
        offspring[3]=mut.inversion_mutation(parents[0])
        offspring[4]=mut.inversion_mutation(parents[1])
        offspring[5]=mut.random_resetting_mutation(parents[1])
        offspring[6]=mut.random_resetting_mutation(parents[0])
        offspring[7]=mut.scramble_mutation(parents[0])
        offspring[8]=mut.scramble_mutation(parents[1])
        offspring[9]=mut.swap_mutation(parents[0])
        offspring[10]=mut.swap_mutation(parents[1])
        offspring[11:13]=cs.multi_point_crossover(parents)
        offspring[13:15]=cs.one_point_crossover(parents)
        offspring[15:17]=cs.uniform_crossover(parents)
        population = np.copy(offspring)
main()
