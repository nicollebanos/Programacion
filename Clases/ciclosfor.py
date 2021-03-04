
for iteracion in range(10):
    print(iteracion)

print("--------------------------")
for iteracion in range(10):
    print(iteracion + 1)

print("--------------------------")
for iteracion in range (1,11):
    print(iteracion)

print("--------------------------")
for iteracion in range (1,14,2):
    print(iteracion)

print("--------------------------")
residuo = 5%4
print(residuo)
residuo = 4%4
print(residuo)

print("--------------------------")
for iteracion in range(1,11):
    if(iteracion%2 == 0):
        print(iteracion)

print("--------------------------")
for iteracion in range(1,11):
    if(iteracion%2 != 0):
        print(iteracion)

print("--------------------------")
for iteracion in range (1,11):
    if(iteracion % 2 == 0):
        print(iteracion, '--> Es un número par')
    else:
        print(iteracion, '--> Es un número impar')