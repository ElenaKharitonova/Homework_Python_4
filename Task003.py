# Задача 3. Выведите число π с заданной точностью. 
# Точность выводится в виде десятичной дроби.
import math

number=int(input('Задайте количество знаков после запятой числа PI:  '))
numbers_pi = round(math.pi, number)
print(numbers_pi)