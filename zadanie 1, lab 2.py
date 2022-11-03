x = int(input("Piersze liczne: "))
y = int(input("Druge liczbe: "))
if x > y:
        x,y = x,y
        print(x)
while x <= y:
    print(x)
    x += 1
