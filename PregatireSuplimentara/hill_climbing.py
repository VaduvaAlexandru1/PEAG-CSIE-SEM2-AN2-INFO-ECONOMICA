import random

def fn(x):
    y = -x ** 2
    return y

def fittness(valoare_curenta , valoare_vecina):
    # if valoare_curenta < valoare_vecina:
    #     return True
    # else:
    #     return False
    return valoare_curenta < valoare_vecina

def hill_climbing(step=0.1 , max=1000000):
    x_curent = random.uniform(-10 , 10)
    y_curent = fn(x_curent) # calculez valoarea functiei in  x curent
    
    for _ in range(max):
        x_vecin = x_curent + random.uniform(-step , step)
        y_vecin = fn(x_vecin)
        
        if fittness(y_curent , y_vecin):
            # x_curent = x_vecin
            y_curent = y_vecin
    
    return y_curent

def main():
    best = hill_climbing()
    print(best)
    
if __name__ == "__main__":
    main()