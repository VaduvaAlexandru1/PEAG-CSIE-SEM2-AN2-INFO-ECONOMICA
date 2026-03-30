import math
import random

def fn(arr):
    return 1 + math.sin(2 * arr[0] - arr[2]) + (arr[1] + arr[3]) ** (1/3)

def fittness():
    pass

def mutatie_neuniforma():
    pass

def gen_pop(dim):
    pop = []
    
    for _ in range(dim):
        pop.append( [
            random.uniform(-1, 1),
            random.uniform(0 , 0.2),
            random.uniform(0 , 1),
            random.uniform(0 , 5)
        ])
        
    return pop

for individ in gen_pop(20):
    print(f"individ : {individ} , value : {fn(individ)}")