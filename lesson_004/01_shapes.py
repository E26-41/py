# -*- coding: utf-8 -*-
from operator import length_hint
from turtledemo.penrose import start

import simple_draw as sd
from simple_draw import get_point

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(point, angle, length):
#    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#    v1.draw()
#
#    v2 = sd.get_vector(start_point=v1.end_point, angle=angle-120,length=length)
#    v2.draw()
#
#    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+120, length=length)
#    v3.draw()
#
# def square(point, angle, length):
#    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#    v1.draw()
#
#    v2 = sd.get_vector(start_point=v1.end_point, angle=angle - 90,length=length)
#    v2.draw()
#
#    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length)
#    v3.draw()
#
#    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 90, length=length)
#    v4.draw()
#
# def pentagon(point, angle, length):
#    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#    v1.draw()
#
#    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72,length=length)
#    v2.draw()
#
#    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length)
#    v3.draw()
#
#    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length)
#    v4.draw()
#
#    sd.line(start_point=v4.end_point, end_point=point)
#
# def hexagon(point, angle, length):
#    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#    v1.draw()
#
#    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60,length=length)
#    v2.draw()
#
#    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length)
#    v3.draw()
#
#    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length)
#    v4.draw()
#
#    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length)
#    v5.draw()
#
#    sd.line(start_point=v5.end_point, end_point=point)
#
#
'''Сделал через встроенные функции simple draw'''
# # def square(point, length, width):
# #     sd.square(left_bottom=point, side=length, width=width)
# #
# # def polygon(point_list, width):
# #     sd.polygon(point_list=point_list, width=width)
# #
# #
# # point1 = sd.get_point(100,100)
# # point2 = sd.get_point(200,100)
# # point3 = sd.get_point(250,200)
# # point4 = sd.get_point(150,280)
# # point5 = sd.get_point(50,200)
# #
# # point6 = sd.get_point(300,100)
# # point7 = sd.get_point(350,150)
# # point8 = sd.get_point(350,200)
# # point9 = sd.get_point(300,250)
# # point10 = sd.get_point(250,200)
# # point11 = sd.get_point(250,150)
# #
# # point_list = [point1, point2, point3, point4, point5]
# # point_list1 = [point6, point7, point8, point9, point10, point11]
#
# # square(point, length, 1)
# # polygon(point_list,1)
# # polygon(point_list1,1)
#
# triangle(sd.get_point(100,100), 60, 150)
# square(sd.get_point(350,100), 90, 150)
# pentagon(sd.get_point(100,300), 15, 100)
# hexagon(sd.get_point(380,300), 15, 100)

# Часть 1-бис.
# Попробуйте прикинуть объем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудьте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы, чтобы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

'''Одной универсальной функцией для каждой фигуры'''
def figures(start_edges, angle, length):
   ''' Получаем координаты '''
   x = start_edges.x
   y = start_edges.y
   for _ in range(3):
      v = sd.get_vector(start_point=start_edges, angle=angle, length=length)
      v.draw()
      start_edges = v.end_point
      angle += 120

   start_edges = sd.get_point(x+300,y)
   for _ in range(4):
      v = sd.get_vector(start_point=start_edges, angle=angle, length=length)
      v.draw()
      start_edges = v.end_point
      angle += 90

   start_edges = sd.get_point(x,y+250)
   start_point = start_edges
   angle = 15
   for _ in range(4):
      v = sd.get_vector(start_point=start_edges, angle=angle, length=100)
      v.draw()
      start_edges = v.end_point
      angle += 72
      if _ == 3:
         sd.line(start_point=start_point, end_point=start_edges)

   start_edges = sd.get_point(x+300,y+250)
   start_point = start_edges
   angle = 15
   for _ in range(5):
      v = sd.get_vector(start_point=start_edges, angle=angle, length=100)
      v.draw()
      start_edges = v.end_point
      angle += 60
      if _ == 4:
         sd.line(start_point=start_point, end_point=start_edges)

figures(sd.get_point(100,100), 20, 150)

sd.pause()
