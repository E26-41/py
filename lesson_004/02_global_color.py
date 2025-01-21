# -*- coding: utf-8 -*-
import simple_draw as sd

colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

print('Возможные цвета:','\n',
      '0 : красный','\n',
      '1 : оранжевый','\n',
      '2 : жёлтый','\n',
      '3 : зелёный','\n',
      '4 : циан','\n',
      '5 : голубой','\n',
      '6 : фиолетовый')

user_input = input('Введите желаемый цвет от 0 до 6 включительно:')
color_num = int(user_input)

if 0 <= color_num <= 6:
    print('Вы ввели:', color_num)
else:
    while color_num < 0 or color_num > 6:
        print('Вы ввели некорректное число, ТАМ ЖЕ ЧЁРНО ПО БЕЛОМОУ НАПИСАНО от 0 до 6 включительно(ГОЙДА)')
        user_input = input('Введите желаемый цвет от 0 до 6 включительно:')
        color_num = int(user_input)
    else:
        print('Вы ввели:', color_num)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def figures(start_edges, angle, length, color):

    ''' Получаем координаты '''
    x = start_edges.x
    y = start_edges.y
    for _ in range(3):
        v = sd.get_vector(start_point=start_edges, angle=angle, length=length)
        v.draw(color=color)
        start_edges = v.end_point
        angle += 120

    start_edges = sd.get_point(x+300,y)
    for _ in range(4):
        v = sd.get_vector(start_point=start_edges, angle=angle, length=length)
        v.draw(color=color)
        start_edges = v.end_point
        angle += 90

    start_edges = sd.get_point(x,y+250)
    start_point = start_edges
    angle = 15
    for _ in range(4):
        v = sd.get_vector(start_point=start_edges, angle=angle, length=100)
        v.draw(color=color)
        start_edges = v.end_point
        angle += 72
        if _ == 3:
            sd.line(start_point=start_point, end_point=start_edges, color=color)

    start_edges = sd.get_point(x+300,y+250)
    start_point = start_edges
    angle = 15
    for _ in range(5):
        v = sd.get_vector(start_point=start_edges, angle=angle, length=100)
        v.draw(color=color)
        start_edges = v.end_point
        angle += 60
        if _ == 4:
            sd.line(start_point=start_point, end_point=start_edges, color=color)

figures(sd.get_point(100,100), 20, 150, colors[color_num])

sd.pause()
