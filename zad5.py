# Zadanie 5

f = open("liczby.txt", "w")
f.write("3\n4\n5")

f = open("liczby.txt", "r")
liczba = f.readlines()

lista = []

for x in liczba:
    lista.append(int(x.strip()))

print((lista[0]**lista[1])+lista[2])

