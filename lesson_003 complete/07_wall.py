# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd    # было без as sd, я добавил для удобства
from simple_draw import COLOR_ORANGE

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x,y = -50, 0
x1, y1 = 50, 50
for _ in range(6):
    for q in range(7):
        point = sd.get_point(x, y)
        point1 = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=point, right_top=point1, color=COLOR_ORANGE, width=1)
        x += 100
        x1 += 100
    x -= 650
    x1 -= 650
    y += 50
    y1 += 50
    for w in range(6):
        point = sd.get_point(x, y)
        point1 = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=point, right_top=point1, color=COLOR_ORANGE, width=1)
        x += 100
        x1 += 100
    x, x1 = -50, 150
    y += 50
    y1 += 50

sd.pause()