
n = int(input("Ile studentow w grupie"))
x = 1
suma = 0
while x<=n :
    punkty = float(input(f"Podaj liczbe punktow dla studenta {x}: "))
    if punkty < 0 or punkty > 100:
        continue
    x = 1 + x
    suma = suma + punkty
print ("średnią liczbę punktów =", suma/n)