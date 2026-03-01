def afis(n):
    for i in range(n):
        print(sol[i], end=' ')
    print()

def verif(k):
    for i in range(k):
        if sol[k] == sol[i]:
            return False
    return True

def solutie(k , n):
    return k == n - 1 

def generare_permutari(k , n):
    for i in range(1, n + 1):  
        sol[k] = i
        if verif(k):
            if solutie(k , n):
                afis(n)
            else:
                generare_permutari(k + 1, n)

def main():
    global sol
    n = int(input("n = "))
    sol = [0] * n
    generare_permutari(0 , n)

if __name__ == "__main__":
    main()