#zadanie 1
x = int(input("Podaj wiek"))
if x < 4:
    print("wstep jest bezplatny")
elif x <= 18:
    print("bilet kosztuje 10zl")
else:
    print("bilet kosztuje 20zl")






#zadanie 1.1
x = int(input("Podaj wiek"))
if x < 4:
cena = 0
elif x <= 18:
cena = 10
else:
cena = 20
print("Cena biletu: {cena} zl")




#zadanie2
literka = input("wprowadz literke")

if len(literka)>1 or len(literka) == 0:
    print("Nieprowidlone dane")
    exit()
if 'a'<= literka <='z':
    print("literka literka jest mala")
elif 'A'<= literka <='Z':
    print("literka jest duza")
else:
    print("podany znak nie jest litera")




#zadanie3
print(''' Jaką operację chcesz wykonać?
1) dodawanie 
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
x = int(input("wpisz numer operacji"))
y = float(input("podaj argument 1"))
z = float(input("podaj argument 2"))
if x == 1:
    wynik = y + z
elif x == 2:
    wynik = y - z
elif x == 3:
    wynik = y * z
elif x == 4:
    wynik = y / z
elif x == 5:
    wynik = y ** z
else:
    print("niepoprawna operacje")
    exit()
print("wynik ")








