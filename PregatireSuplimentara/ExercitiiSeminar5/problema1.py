import random

def fn(permutari):
    count = 0
    for i in range(len(permutari)):
        for j in range(i + 1 , len(permutari)):
            if permutari[i] < permutari[j]:
                count += 1
    return count

def gen_pop(dim , n):
    pop = []
    
    for _ in range(dim):
        individ = list(range(1 , n + 1))
        random.shuffle(individ)
        
        individ = individ + [fn(individ)]
        pop.append(individ)
    
    return pop

def mutatie_interchimbare(individ):
    individ = individ[:-1]
    i , j = random.sample(range(len(individ)) , 2)
    individ[i] , individ[j] = individ[j] , individ[i]
    
    individ += [fn(individ)]
    return individ
    
def gen_new_pop(pop , pm):
    new_pop = []
    for individ in pop:
        r = random.uniform(0 , 1)
        if r < pm:
            individ = mutatie_interchimbare(individ)
        new_pop.append(individ)
    return new_pop
        

pop = gen_pop(5, 4)
print("Pop initiala:")
for ind in pop:
    print(ind)

pop_mutata = gen_new_pop(pop, 0.3)
print("\nPop dupa mutatie:")
for ind in pop_mutata:
    print(ind)
    
    