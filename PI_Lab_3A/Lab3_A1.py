try:
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
except:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

if(x1 > 0 and x2 > 0):
    if(y1 > 0 and y2 > 0):
        print("YES")
        print("I")
    elif(y1 < 0 and y2 < 0):
        print("YES")
        print("IV")

elif(x1 < 0 and x2 < 0):
    if(y1 > 0 and y2 > 0):
        print("YES")
        print("II")
    elif(y1 < 0 and y2 < 0):
        print("YES")
        print("III")

else:
    print("NO")
