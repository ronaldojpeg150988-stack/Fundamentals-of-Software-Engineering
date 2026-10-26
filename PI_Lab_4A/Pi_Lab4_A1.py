import random
import time

try:
    numberOfExamples = int(input("Введите количество примеров: "))
    numberOfSolvedExamples = 1
    numberOfCorrectExamples = 0
    totalTime = 0
except:
    print("Введите целое число.")

while(numberOfSolvedExamples <= numberOfExamples):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    timeForExample = 0
    print(f"Вопрос {numberOfSolvedExamples}/{numberOfExamples}")
    c = None
    while(c is None):
        try:
            startTime = time.time()
            c = int(input(f"{a}*{b}="))
            timeForExample = round(time.time() - startTime, 2)
        except:
            print("Введите целое число!")
    if (a*b == c):
        numberOfCorrectExamples = numberOfCorrectExamples + 1
        print(f"Верно! (Время: {timeForExample} сек).")
    else:
        print(f"Неверно! Правильно: {a * b}. (Время: {timeForExample} сек).")
    totalTime = totalTime + timeForExample
    numberOfSolvedExamples = numberOfSolvedExamples + 1
    
averageTime = round(totalTime / numberOfExamples, 2)
percentageCorrect = round(numberOfCorrectExamples/numberOfExamples * 100, 1)
print("=====================================")
print("СТАТИСТИКА:")
print("=====================================")
print(f"Общее время: {totalTime} секунд\nСреднее время на вопрос: {averageTime}\nПравильных ответов: {numberOfCorrectExamples}/{numberOfExamples}\nПроцент правильных: {percentageCorrect}%")

