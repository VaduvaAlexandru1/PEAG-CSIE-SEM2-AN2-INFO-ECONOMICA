# Variabila fara continut
x = None

#Variabila globala
global y
y = 10
# gresit !!! global y = 10

# boolean cu T si F mare , gresit true , false , corect True , False
ok = True

# pentru tipuri
print(type(x))

# returneaza True sau False 
print(isinstance(x , int))

# arrays

numere = [1 , 2 , 3 , 4]
numere.append(5)
print(numere)

pp = [h * h for h in numere]

# Check existance in array
print(1 in numere)

# Tuples
print('--------------Tuples------------------')
punct = (3 , 4)

print(punct)
x , y = punct
print(x)
print(y)

# Set

print('-----------------Set---------------------')
numere_set = {1 , 2 , 3 , 4}
numere_set.add(5)
print(numere_set)

# Dictionare

print('------------Dictionare-------------')

student = {
    "nume" : "Andrei",
    "varsta" : 20,
    "bani" : True
}

varsta = student.get('varsta')
nume = student['nume']
print(varsta)
print(nume)

#dictionary comprehension
student2 = {key : key for key in student}

# Conditionale

print('--------------Conditionale---------------')
x = 9

if x > 11:
    print('ok')
elif x < 10:
    print('elif')
else:
    print('else')

print('-----------Ternar---------------')
par = 'Par' if 3 % 2 == 0 else 'Impar'
print(par)


# Loops

print('---------For Loops----------------')

array2 = [1 , 2 , 3 , 4 , 5]


for i in range(1 , 5 , 2):
    print(array2[i])
    
# for num in array2:
#     print(num)

# nu exista operatori de incrementare / decrementare "gresit x++ sau x--"

# functii 
print('--------------Functii-----------------')
def putere(x , exp=1):
    return x ** exp

print(putere(4))
print(putere(4 , 2))
print(putere(4 , 3))

pp = lambda x : x*x

# F string
print('----------F string------------')
varsta = 20

print('Andre are ' + str(varsta) + ' de ani')
print(f"Andrei are {varsta} ani")
