# Zadanie 8

lista = []
i=0

while i < 10:
    a = input("Wprowadź liczbę: ")
    a = int(a)
    if a%2==0:
        lista.append(a)
        i += 1
    else:
        i += 1

print(lista)