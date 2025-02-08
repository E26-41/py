# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(start_point, angle, length):
#     v = sd.get_vector(start_point=start_point, angle=angle-30, length=length)
#     v.draw()
#     v = sd.get_vector(start_point=start_point, angle=angle+30, length=length)
#     v.draw()

# draw_branches(sd.get_point(250,225), 90, 50)

def draw_branche(start_point, angle, length):
    v = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v.draw()
    start_point1, start_point2 = v.end_point, v.end_point
    angle1, angle2 = v.angle, v.angle
    point = [start_point1, start_point2]
    draw_branches(point, angle1, angle2, length)

def draw_branches(point, angle1, angle2, length):
    if length <= 10:
        return
    for start_point in point:
        v1 = sd.get_vector(start_point=start_point, angle=angle1-30, length=length)
        v1.draw()
        v2 = sd.get_vector(start_point=start_point, angle=angle2-30, length=length)
        v2.draw()
        point += [v1.end_point, v2.end_point]
        angle1, angle2 = v1.angle, v2.angle
    length = length * 0.75
    draw_branches(point, angle1, angle2, length)

draw_branche(sd.get_point(300,100), angle=90, length=150)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


