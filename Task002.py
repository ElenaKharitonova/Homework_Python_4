# Задача 2. В первой строке файла находится 
# информация об ассортименте мороженного, 
# во второй - информация о том,какое мороженное есть 
# на складе. Выведите названия того товара, 
# который закончился.

data = open('Icecream.txt', mode = 'r', encoding='utf-8')
icecream=data.readlines()
data.close()
print(icecream)

assortment = set(icecream[0].replace('\n', '').split(', '))
available = set(icecream[1].replace('\n', '').split(', '))
result = assortment-available
print(f'На складе отсутствует мороженое: {result}')  