#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, 'beer')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

# Первый способ
zoo = zoo + birds
print(zoo)
del zoo[5:]
print(zoo)

# Второй способ
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль

# Первый способ
zoo.remove('elephant')
print(zoo)

zoo.insert(3, 'elephant')
print(zoo)

# Второй способ
del zoo[3]
print(zoo)

# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

print('Лев сидит в клетке под номером',zoo.index('lion') +1,', а жаворонок в клетке',zoo.index('lark') +1)