import copy
import random

def fittness(individ):
    return sum(individ)

def gen_pop(dim):
    pop = []
    
    for _ in range(dim):
    
        individ = random.choices([0 , 1] , k=7)
        individ.append(fittness(individ))
        
        pop.append(individ)
    
    return pop

def cerinta_b(pop, pc):
    pop_copy = copy.deepcopy(pop)
    
    def two_point_crossover(p1, p2):
        i, j = sorted(random.sample(range(1, 6), 2))
        res1 = p1[:i] + p2[i:j] + p1[j:]
        res2 = p2[:i] + p1[i:j] + p2[j:]
        return res1, res2
    
    def gen_new_pop():
        for i in range(0, len(pop) - 1, 2):
            r = random.uniform(0, 1)
            if r < pc:
                c1, c2 = two_point_crossover(pop[i][:-1], pop[i+1][:-1])
                c1.append(fittness(c1))
                c2.append(fittness(c2))  # fixed here
                pop_copy[i] = c1.copy()
                pop_copy[i + 1] = c2.copy()
    
    gen_new_pop()
    return pop_copy