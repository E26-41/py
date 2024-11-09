# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
'''
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)
'''
# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius)
'''
point = sd.get_point(300, 300)
bubble(point=point, step = 10 )

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1100, 100):
    point = sd.get_point(x, 500)
    bubble(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков

for y in range(100, 301, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=10)
'''
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=3)

sd.pause()


