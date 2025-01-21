# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

print('Возможные фигуры:','\n',
      '0 : треугольник','\n',
      '1 : квадрат','\n',
      '2 : пятиугольник','\n',
      '3 : шестиугольник')

user_input = input('Введите желаемую от 0 до 3 включительно:')
figure_num = int(user_input)

if 0 <= figure_num <= 3:
    print('Вы ввели:', figure_num)
else:
    while figure_num < 0 or figure_num > 3:
        print('Вы ввели некорректное число, ТАМ ЖЕ ЧЁРНО ПО БЕЛОМОУ НАПИСАНО от 0 до 6 включительно(ГОЙДА)')
        user_input = input('Введите желаемый цвет от 0 до 3 включительно:')
        figure_num = int(user_input)
    else:
        print('Вы ввели:', figure_num)

def figures(start_edges, angle, length, num_of_figure):
    if num_of_figure == 0:
        for _ in range(3):
            v = sd.get_vector(start_point=start_edges, angle=angle, length=length)
            v.draw()
            start_edges = v.end_point
            angle += 120

    elif num_of_figure == 1:
        for _ in range(4):
            v = sd.get_vector(start_point=start_edges, angle=angle, length=length)
            v.draw()
            start_edges = v.end_point
            angle += 90

    elif num_of_figure == 2:
        start_point = start_edges
        angle = 15
        for _ in range(4):
            v = sd.get_vector(start_point=start_edges, angle=angle, length=100)
            v.draw()
            start_edges = v.end_point
            angle += 72
            if _ == 3:
                sd.line(start_point=start_point, end_point=start_edges)
    else:
        start_point = start_edges
        angle = 15
        for _ in range(5):
            v = sd.get_vector(start_point=start_edges, angle=angle, length=100)
            v.draw()
            start_edges = v.end_point
            angle += 60
            if _ == 4:
                sd.line(start_point=start_point, end_point=start_edges)

figures(sd.get_point(250,225), 20, 150, figure_num)
sd.pause()
