# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd    # Изменил как в 7 домашке

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: координата X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smileface(point, color, width):

    ''' Рисуем тело для смайлика '''
    radius = 50
    sd.circle(center_position=point, radius=radius, color=color,  width=width)

    ''' Получаем координаты '''
    x = point.x
    y = point.y

    ''' Меняем полученные координаты и делаем глазки '''
    x += 20
    y += 10
    right_eye = sd.get_point(x, y)
    radius = 10
    sd.circle(center_position=right_eye, radius=radius, color=color, width=width)
    x -= 40
    left_eye = sd.get_point(x, y)
    sd.circle(center_position=left_eye, radius=radius, color=color, width=width)

    ''' Делаем рот '''
    x = point.x
    y = point.y

    x1 = x - 30
    y1 = y - 10
    point1 = sd.get_point(x1, y1)

    x2 = x - 10
    y2 = y - 25
    point2 = sd.get_point(x2, y2)

    x3 = x + 10
    point3 = sd.get_point(x3, y2)

    x4 = x + 30
    point4 = sd.get_point(x4, y1)
    coordinates = [point1, point2, point3, point4]
    lines = sd.lines(point_list=coordinates, color=color, width=width)

for _ in range(10):
    point = sd.random_point()
    color = sd.random_color()
    smileface(point=point, color=color, width=3)

sd.pause()