import random

p = int(input("Enter p:"))
g = int(input("Enter g:"))

a = random.randint(1, 100)      
b = random.randint(1, 100)

x = ((g ** a) % p)           
y = ((g ** b) % p)

Ka = ((y ** a) % p)
Kb = ((x ** b) % p)

print("Secret key at A = ", str(Ka))
print("Secret key at B = ", str(Kb))
