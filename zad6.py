# Zadanie 6

a = input("Wprowadź liczbę pierwszą: ")
b = input("Wprowadź liczbę drugą: ")
c = input("Wprowadź liczbę trzecią: ")

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print("Największa liczba to: ", a)
elif b > a and b > c:
    print("Największa liczba to: ", b)
else:
    print("Największa liczba to: ", c)
