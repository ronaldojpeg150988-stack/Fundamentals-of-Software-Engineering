try:
    prRd = int(input("Previous readings: "))
    cuRd = int(input("Current reading: "))

    if (prRd > cuRd):
        print("Incorrect values")
    else:
        used = cuRd - prRd

        if (used <= 300):
            price = 21
        elif (used <= 600):
            price = 21 + (used - 300) * 0.06
        elif (used <= 800):
            price = used * 0.04
        else:
            price = used * 0.025
        
        avPrice = price / used

        print("Предыдущее    Текущее     Использовано    К оплате    Ср. цена m^3")
        print(f"  {prRd}           {cuRd}             {used}            {price}           {round(avPrice, 2)}")
except:
    print("")
