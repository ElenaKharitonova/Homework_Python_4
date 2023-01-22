# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список 
# простых множителей числа N.

n=int(input('Задайте натуральное число:  '))
result = []
count = 2
while n != 1 & count <= n+1:
    while n % count ==0:
        result.append(count)
        n//= count
    count+=1        
print (result)