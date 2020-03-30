import client as cl
import random as rand
import numpy as np 
import crossover as cs
import mutation as mut
import selection as sel
key = '4scAFELWNu1oZKJ7xovrpF4uMhuOAtUNizeYl9cAIVx5F8Vp72'

def generate_population():
    new_gen = np.random.uniform(low = -10 , high = 10 , size=(16,11))
    new_gen[0] = file_input()
    for i in range(1,16):
        new_gen[i] = mut.random_setting_mutation(new_gen[0])
    return (new_gen)

def file_input():
    model = open('overfit.txt')
    model = model.read()
    mode = np.fromstring(model.replace("[","").replace("]","",).replace(",","   "),sep="    ")
    return mode

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
        np.save('example',population)
        np.save('error',fitness)
        print(population,fitness)
        offspring = np.zeros((16,11))
        offspring[0:2]= sel.rank_selection(population,fitness)
        offspring[2] = sel.roulette_selection(population,fitness)
        offspring[3] = sel.roulette_selection(population,fitness)
        for i in range(4,10):
            offspring[i] = mut.random_setting_mutation(offspring[rand.randint(0,4)])
        for i in range(10,16):
            first = rand.randint(0,4)
            second = rand.randint(0,4)
            while first is not second:
                second = rand.randint(0,4)
            offspring[i] = cs.mutation_crossover(np.array([offspring[first],offspring[second]]))
        population = np.copy(offspring)
        print(cl.submit(key,np.ndarray.tolist(offspring[0])))
        print(cl.submit(key,np.ndarray.tolist(offspring[1])))
        print(cl.submit(key,np.ndarray.tolist(offspring[2])))
        print(cl.submit(key,np.ndarray.tolist(offspring[3])))
main()