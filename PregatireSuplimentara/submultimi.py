def afis(n):
    for i in range(1, n + 1):
        if sol[i] == 1:  
            print(i, end=' ')
    print()

def generare_submultimi(k, n):
    if k > n:  
        afis(n)
        return
    sol[k] = 1
    generare_submultimi(k + 1, n)
    sol[k] = 0
    generare_submultimi(k + 1, n)

def main():
    global sol
    n = int(input("n= "))
    sol = [0] * (n + 1)  
    generare_submultimi(1, n)

if __name__ == "__main__":
    main()