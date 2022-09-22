a = float(input(""))

while (a < 0) or (a > 10):
    print("nota invalida")
    a = float(input(""))

b = float(input(""))

while (b < 0) or (b > 10):
    print("nota invalida")
    b = float(input(""))

Media = (a+b) / 2
print("media = " + str(Media))
