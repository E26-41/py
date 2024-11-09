# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 10 с шагом 11 из точки (50, 50) в точку (350, 450)

sd.resolution = (800, 500)
x1 = 50
y1 = 350
z = 0
for _ in range(7):
    x = sd.get_point(x1, 50)
    y = sd.get_point(y1, 450)
    sd.line(start_point=x, end_point=y, color=rainbow_colors[z], width=10)
    x1 += 11
    y1 += 11
    z +=1

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(801, 0)
radius = 200
z = 6
for _ in range(7):
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[z], width=35)
    radius += 35
    z -= 1

sd.pause()