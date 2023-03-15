# [{'dishes':..., "ingredient_name"}]
# {'Омлет': [...], 'Утка по-пекински': [...], 'Запеченный картофель': [...]}
import pprint

with open('Two_1') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        quantity_count = int(file.readline())
        dishess = []
        for _ in range(quantity_count):
            quan = file.readline().strip()
            ingredient_name, quantity, measure = quan.split(' | ')
            dishess.append(
                {'ingredient_name':  ingredient_name,
                 'quantity': quantity,
                 'measure': measure}
            )
        cook_book[dishes] = dishess
        file.readline()
print(cook_book)