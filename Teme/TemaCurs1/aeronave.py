from Aeronava import Aeronava
import random
import copy

suma_disponibila = 5000
vizibiliate_minima = 2000

def pret_total(aeronave):
    suma = 0
    for aeronava in aeronave:
        suma += aeronava.cost * aeronava.cantitate
    return suma

def autonomie_medie(aeronave):
    suma = 0
    cantitate_totala = 0
    for aeronava in aeronave:
        suma += aeronava.autonomie * aeronava.cantitate
        cantitate_totala += aeronava.cantitate
    return suma / cantitate_totala

def vizibilitate_medie(aeronave):
    suma = 0
    cantitate_totala = 0
    for aeronava in aeronave:
        suma += aeronava.vizibilitate_minima * aeronava.cantitate
        cantitate_totala += aeronava.cantitate
    return suma / cantitate_totala
        
def fittness(aeronave_curente , aeronave_vecine):
    if pret_total(aeronave_vecine) > suma_disponibila or pret_total(aeronave_curente) < pret_total(aeronave_vecine):
        return False
    
    if autonomie_medie(aeronave_curente) < autonomie_medie(aeronave_vecine):
        return False
    
    if vizibilitate_medie(aeronave_curente) < vizibilitate_medie(aeronave_vecine) or vizibilitate_medie(aeronave_vecine) < vizibiliate_minima:
        return False
    return True

def genereaza_vecin(aeronave):
    vecin = copy.deepcopy(aeronave)
    
    index = random.randint(0 , 2)
    modif = random.choice([1 , -1])
    
    if vecin[index].cantitate + modif >= 0:
        vecin[index].cantitate += modif
        
    return vecin
    
    

def hill_climbing(solutie , max_iter=10000):
    
    for _ in range(max_iter):
        vecin = genereaza_vecin(solutie)
        
        if fittness(solutie , vecin):
            solutie = vecin
    
    return solutie

def main():
    solutie = []
    while True:
        solutie = [
                Aeronava("I", random.randint(0, 50), 100, 6000, 1500),
                Aeronava("II", random.randint(0, 50), 60, 4200, 2400),
                Aeronava("III", random.randint(0, 50), 50, 2800, 1600)
            ]
        if pret_total(solutie) <= suma_disponibila and vizibilitate_medie(solutie) >= vizibiliate_minima:
            break
    
    best = hill_climbing(solutie)
    
    for aeronava in best:
        aeronava.afis()

    print("Cost total:", pret_total(best))
    print("Autonomie medie:", autonomie_medie(best))
    print("Vizibilitate medie:", vizibilitate_medie(best))
    
if __name__ == '__main__':
    main()