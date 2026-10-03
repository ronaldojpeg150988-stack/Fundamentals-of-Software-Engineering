A = int(input("Input A: "))
if (A > 1000 or A < 1):
    print("Invalid value")
B = int(input("Input B: "))
if (B > 1000 or B < 1):
    print("Invalid value")
else:
    if (A == B):
        print("The numbers are equal.")
    else:
        if (A > B):
            print("A is greater than B")
        elif(A < B):
            print("B is greater than A")
