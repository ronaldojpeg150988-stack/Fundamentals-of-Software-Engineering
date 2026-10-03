x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

if ((x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0):
    print("YES")
    print("White")

elif ((x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0):
    print("YES")
    print("Black")

else:
    print("NO")

