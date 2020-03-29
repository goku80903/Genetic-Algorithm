import numpy as np
import random as rand
def tournament_selection(generation,fitness,k):
    individuals = np.random.randint(low = 0 , high = len(fitness) , size = (k))
    ma = 10e100
    index = 0
    for i in individuals:
        if ma > fitness[i][0]+fitness[i][1]:
            index = i
            ma = fitness[i][0]+fitness[i][1]
    offspring = np.copy(generation[index])
    return offspring

def roulette_selection(generation,fitness):
    select = np.sum(fitness,axis=1)
    temp = np.full(len(generation),np.max(select))
    temp = np.subtract(temp,select)
    Sum = np.sum(temp)
    random_number = rand.uniform(0,Sum)
    for i in range(0,len(generation)):
        random_number+=temp[i]
        if(random_number>Sum):
            return generation[i]

def rank_selection(generation,fitness):
    select = np.copy(fitness)
    select = select[:,1]*0.7 + select[:,0]*0.3
    select = np.reshape(select,(-1,1))
    select = np.append(generation,select,axis=1)
    select = select[select[:,11].argsort()]
    return select[0:2,0:11]

def rank_selection2(generation,fitness):
    select = np.copy(fitness)
    select = select[:,1]*0.7 + select[:,0]*0.3
    select = np.reshape(select,(-1,1))
    select = np.append(generation,select,axis=1)
    select = select[select[:,11].argsort()]
    return select[0:2,0:11]