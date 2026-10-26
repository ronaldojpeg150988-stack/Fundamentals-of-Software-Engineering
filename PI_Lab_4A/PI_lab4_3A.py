packets = input()
if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    deliverd = 0
    lost = 0
    sequence = 0
    maxSequence = 0

    for packet in packets:
        if packet == '0':
            lost += 1
            sequence +=1
            if (sequence >= maxSequence):
                maxSequence = sequence
        elif packet == '1':
            deliverd += 1
            sequence = 0

    percent = round(lost/len(packets) * 100, 1)
    print(f"Общее количество пакетов: {len(packets)}")
    print(f"Количество потерянных пакетов: {lost}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {maxSequence}")
    print(f"Процент потерь: {percent}%")
    print("Качество связи: ", end = '')
    if (percent <= 1):
        print(" Отличное качество")
    elif (percent <= 5):
        print(" Хорошее качество")
    elif (percent <= 10):
        print(" Удовлетворительное качество")
    elif (percent <= 20):
        print(" Плохое качество")
    elif (percent > 20):
        print(" Критическое состояние сети")

