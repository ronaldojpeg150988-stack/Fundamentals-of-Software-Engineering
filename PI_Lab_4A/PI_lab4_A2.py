
from random import weibullvariate


def drawRectangle(rows, columns, ch = '#'):
    for i in range(rows):
       print()
       for j in range(columns):
          print(ch, end = '')

def drawTriangle(height, ch):
    for i in range(height):
        print()
        for j in range(i + 1):
           print(ch, end = '')

def drawFrame(height, width, ch):
    for i in range(height):
       print()
       if(i == 0 or i == height - 1):
           for j in range(width):
               print(ch, end = '')
       else:
           for j in range(width):
               if(j == 0 or j == m - 1):
                   print(ch, end = '')
               else:
                   print(" ", end = '')





try:
    n = int(input("ПЯМОУГОЛЬНИК Высота: "))
    m = int(input("Ширина: "))
    ch = input("Символ: ")
    drawRectangle(n, m, ch)

except:
    print("Неверные значения!")


try:
    n = int(input("\n\nПРАВЫЙ ТРЕУГОЛЬНИК Высота: "))
    ch = input("Символ: ")
    drawTriangle(n, ch)
except:
    print("Неверные значения!")


try:
    n = int(input("\n\nРАМКА Высота: "))
    m = int(input("Ширина: "))
    ch = input("Символ: ")
    drawFrame(n, m, ch)
except:
    print("Неверные значения!")


print()