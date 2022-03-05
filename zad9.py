# Zadanie 9

import math

a = input("Wprowadź liczbę: ")

a = int(a)

if a < 0:
    print("Nie można policzyć pierwiastka z liczby ujemnej: ")
else:
    print(math.sqrt(a))