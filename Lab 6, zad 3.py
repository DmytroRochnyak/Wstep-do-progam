"""Zadanie 3. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę"""



def funkcja(*args):
    print(type(args))
    print(args)
    for i in args:
        print(i)

funkcja(49,48.31, "String", [1,3,5])
funkcja()
funkcja(91, 196)