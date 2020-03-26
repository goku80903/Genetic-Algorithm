import numpy as np
import random as rand
def random_resetting_mutation(parent):
    temp = np.copy(parent)
    invert = int(rand.uniform(0,11))
    while not invert:
        invert = int(rand.uniform(0,11))
    random_number = rand.uniform(-10,10)
    temp[invert] = random_number
    return temp

def swap_mutation(parent):
    temp = np.copy(parent)
    invert1 = int(rand.uniform(0,10))
    while not invert1:
        invert1 = int(rand.uniform(0,11))
    invert2 = int(rand.uniform(invert1+1,11))
    temp[invert1] , temp[invert2] = temp[invert2] , temp[invert1]
    return temp

def scramble_mutation(parent):
    temp = np.copy(parent)
    invert1 = int(rand.uniform(0,10))
    while not invert1:
        invert1 = int(rand.uniform(0,11))
    invert2 = int(rand.uniform(invert1+1,11))
    temp[invert1:invert2] = np.random.permutation(temp[invert1:invert2])
    return temp

def inversion_mutation(parent):
    temp = np.copy(parent)
    invert1 = int(rand.uniform(0,10))
    while not invert1:
        invert1 = int(rand.uniform(0,11))
    invert2 = int(rand.uniform(invert1+1,11))
    temp[invert1:invert2] = np.flip(temp[invert1:invert2])
    return temp