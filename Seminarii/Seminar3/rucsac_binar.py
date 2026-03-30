import numpy as np
import random

def ok(x , c , v , max):
    val = np.dot(x , v)
    cost = np.dot(x , c)
    return cost <= max ,val

def reprezinta_pop(x , c , v , max):
    x = [i for i in range(max)]

def gen(fc , fv , max , dim):
    c = np.genfromtxt(fc)
    v = np.genfromtxt(fv)
    n = v.size
    pop = []
    
    for i in range(dim):
        gata = False
        while gata is not True:
            x = random.choices([0 , 1] , k=n)
            gata,val = ok(x , c , v , max)
        x.append(val)
        pop.append(x)
    reprezinta_pop(pop , dim , n)
    return pop
