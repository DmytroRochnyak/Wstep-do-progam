x = int(input("Piersze liczne: "))
y = int(input("Druge liczbe: "))
if x > y:
        x,y = x,y
        print(x)
while x <= y:
    if x%2 == 1:
        x = x + 1
        continue

    print(x)
    x += 1