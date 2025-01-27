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
#     v = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
#     v.draw()
#     v = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
#     v.draw()
#
# draw_branches(sd.get_point(250,225), 90, 50)

def draw_branches_re(start_point, angle, length, delta):
    if length <= 10:
        return
    v = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v.draw()
    v1 = sd.get_vector(start_point=start_point, angle=angle+30, length=length)
    v1.draw()
    start_point = v.end_point
    start_point1 = v1.end_point
    angle = angle - delta
    length = length * 0.75
    draw_branches_re(start_point, angle, length, delta)
    draw_branches_re(start_point1, angle, length, delta)


for delta in range(10, 20, 10):
    draw_branches_re(sd.get_point(300,0), angle=90, length=150, delta=delta)
for delta in range(-10, -9, 10):
    draw_branches_re(sd.get_point(300,0), angle=90, length=150, delta=delta)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


