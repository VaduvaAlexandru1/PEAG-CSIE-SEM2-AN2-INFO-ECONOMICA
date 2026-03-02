import random

def fn(input):
    return input[0]**2 - 2*input[1]*input[2]

def fittness(candidat):
    return candidat[0] + candidat[1] + candidat[2] < 10

def gen_candidat():
    candidat = [random.uniform(-2 ,7) , random.uniform(-2 , 7) , random.uniform(-2,7)]
    while fittness(candidat) is not True:
        candidat = [random.uniform(-2 ,7) , random.uniform(-2 , 7) , random.uniform(-2,7)]
    return candidat
        

def main():
    for _ in range(20):
        candiat = gen_candidat()
        print(f"x={candiat[0]} , y={candiat[1]} , z={candiat[2]} , valoare={fn(candiat)}")
        
main()
    