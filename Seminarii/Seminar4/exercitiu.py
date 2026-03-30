import random

def fn(x , y , z):
    return x + y - 2 * z

#functia fitness
def fitness(x , y , z):
    return x**3 + 2 * y - 3 * z < 14 , fn(x , y, z)

def gen_pop(a , b , max):
    pop = []
    for _ in range(max):
        ready = False
        while not ready:
            x = [random.uniform(a , b) for _ in range(3)]
            ready , val = fitness(x[0] , x[1] , x[2])
        
        x.append(val)
        pop.append(x)
    
    return x

def mutatie(pop , a , b , max , pm):
    mpop = pop.deepcopy(pop)