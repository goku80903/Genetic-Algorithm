import random as rand
import numpy as np

def file_input():
    model = open('overfit.txt')
    model = model.read()
    mode = np.fromstring(model.replace("[","").replace("]","",).replace(",","   "),sep="    ")
    return mode

def one_point_crossover(parents):
    offsprings = np.zeros((2,11))
    invert = int(rand.uniform(0,11))
    while not invert:
        invert = int(rand.uniform(0,11))
    offsprings[0] = np.append(parents[0,0:invert],parents[1,invert:len(parents[0])+1])
    offsprings[1] = np.append(parents[1,0:invert],parents[0,invert:len(parents[0])+1])
    return offsprings

def multi_point_crossover(parents):
    offsprings = np.copy(parents)
    invert1 = int(rand.uniform(0,10))
    while not invert1:
        invert1 = int(rand.uniform(0,11))
    invert2 = int(rand.uniform(invert1+1,11))
    temp = np.copy(offsprings[0])
    offsprings[0,invert1:invert2] = offsprings[1,invert1:invert2]
    offsprings[1,invert1:invert2] = temp[invert1:invert2]
    return offsprings

def uniform_crossover(parents):
    offsprings = np.copy(parents)
    invert = np.random.randint(low = 0, high = 10 , size=(6))
    for i in invert:
        offsprings[0,i] , offsprings[1,i] = offsprings[1,i] , offsprings[0,i]
    return offsprings

def mutation_crossover(parents):
    offspring = np.zeros((11))
    overfit = file_input()
    for i in range(11):
        prob = rand.random()
        if prob<0.3 : 
            offspring[i] = parents[0,i]
        elif prob<0.6 :
            offspring[i] = parents[1,i]
        elif prob<0.8 :
            offspring[i] = overfit[i]
        else:
            offspring[i] = parents[rand.randint(0,1),i]*rand.uniform(-2,2)
    return offspring