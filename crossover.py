import random as rand
import numpy as np
def one_point_crossover(parents):
    offsprings = np.zeros((2,11))
    invert = int(rand.uniform(0,11))
    while not invert:
        invert = int(rand.uniform(0,11))
    print(invert,len(parents[0]))
    print(parents[0])
    print(parents[1])
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
    print(invert)
    print(parents)
    for i in invert:
        offsprings[0,i] , offsprings[1,i] = offsprings[1,i] , offsprings[0,i]
    print(offsprings)
