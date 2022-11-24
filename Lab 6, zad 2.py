"""Zadanie 2. Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania."""



def oblicz(x,y):
    roz = x - y
    sum = x + y
    return roz, sum
    print(f"Suma: {sum} Roznica: {roz}")
a = int(input("Podaj x: "))
b = int(input("Podaj y: "))

w = oblicz(24.13, 13.56)
print(w[0], w[1])

a,b = oblicz(56,34.78)
print(a,b)