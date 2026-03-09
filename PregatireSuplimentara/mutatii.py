import random
import copy
import math
# x + y - 2z  < 14, x^3 + 2y - 3z , [-7 , 15]

def fn(valori):
    # x = valori[0]
    # y = valori[1]
    # z = valori[2]
    
    # output = x ** 3 + 2 * y - 3 * z
    
    # # return output
    return valori[0] **3 + 2 * valori[1] - 3 * valori[2]


def fitness(valori):
    
    # x = valori[0]
    # y = valori[1]
    # z = valori[2]
    
    # verif = False
    
    # if x + y - 2 * z < 14:
    #     verif = True
    # else :
    #     verif = False
        
    # return verif
    
    return valori[0] + valori[1] - 2 * valori[2] < 14

def gen_pop(a , b , max):
    pop = []
    
    for _ in range(max):
        individ = [random.uniform(a , b) for _ in range(3)]
        while fitness(individ) is False:
            individ = [random.uniform(a , b) for _ in range(3)]
        
        pop.append(individ)
        
    return pop

def mutatie_uniforma(a , b , pop , pm):
    pop_noua = []
    
    for individ in pop:
        individ_nou = []
        copie = copy.deepcopy(individ)
        # copie = [gena for gena in individ]
        for gena in individ:
            r = random.uniform(0 , 1)
            if r < pm:
                gena = random.uniform(a , b)

            individ_nou.append(gena)
        #verificare daca individ nou este fezabil
        if fitness(individ_nou):
            pop_noua.append(individ_nou)
        else:
            pop_noua.append(copie)
    return pop_noua

def mutatie_neuniforma_cu_pas(a , b , pas, pop , pm):
    pop_noua = []
    
    for individ in pop:
        individ_nou = []
        copie = copy.deepcopy(individ)
        for gena in individ:
            r = random.uniform(0 , 1)
            if r < pm:
                epsilon = random.uniform(-pas , pas)
                gena += epsilon
                
                gena = max(a , min(b , gena))
                
                # if gena > b :
                #     gena = b
                # if gena < a:
                #     gena = a

            individ_nou.append(gena)
        #verificare daca individ nou este fezabil
        if fitness(individ_nou):
            pop_noua.append(individ_nou)
        else:
            pop_noua.append(copie)
    return pop_noua

def mutatie_neuniforma_gauss(a , b , sigma, pop , pm):
    pop_noua = []
    
    for individ in pop:
        individ_nou = []
        copie = copy.deepcopy(individ)
        for gena in individ:
            r = random.uniform(0 , 1)
            if r < pm:
                print("mutat")
                epsilon = random.gauss(0 , math.sqrt(sigma))
                gena += epsilon
                
                gena = max(a , min(b , gena))
                
                # if gena > b :
                #     gena = b
                # if gena < a:
                #     gena = a

            individ_nou.append(gena)
        # verificare daca individ nou este fezabil
        
        # optimizare pentru codul curent noi adaugam oricum gena curenta daca nu este mutata , prin urmare ne putem lipsi de else si de copie 
        # deoarece daca nu avem mutatii pe nicio gena atunci individul este acelasi 
        if fitness(individ_nou):
            pop_noua.append(individ_nou)
        else:
            pop_noua.append(copie)
    return pop_noua

    

def main():
    pop  = gen_pop(-7 , 15 , 20)
    pop_mutata_pas = mutatie_neuniforma_cu_pas(-7 , 15 , 0.02 , pop , 0.1)
    pop_mutata_gaus = mutatie_neuniforma_gauss(-7 , 15 , 0.02 , pop , 0.1)
    pop_mutata_uniform = mutatie_uniforma(-7 , 15 , 20)
    for individ in pop_mutata_gaus:
        print(individ)
    
main()

