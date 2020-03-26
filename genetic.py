import client as cl
import random as rand
import numpy as np 
import crossover as cs
import mutation as mut
key = '4scAFELWNu1oZKJ7xovrpF4uMhuOAtUNizeYl9cAIVx5F8Vp72'

def generate_population():
    new_gen = np.random.uniform(low = -10 , high = 10 , size=(10,11))
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
    return sorted(fitness,key= lambda x:x[0])

parent = np.random.uniform(-10,10,size = (11))