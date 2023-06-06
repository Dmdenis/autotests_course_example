# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


with open('test_file/task_3.txt', mode='r', encoding='utf-8') as total:
    purchase_list = [[]]
    for line in total.readlines():
        if line == '\n':
            purchase_list.append([])
        else:
            purchase_list[-1].append(int(line))
for index, value in enumerate(purchase_list):
    purchase_list[index] = sum(value)

three_most_expensive_purchases = sum(sorted(purchase_list)[-3:])


assert three_most_expensive_purchases == 202346
