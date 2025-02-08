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

# sd.resolution = (1400, 1000)
# def draw_branch(start_point, angle, length):
#     v = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v.draw()
#     draw_branches(point=v.end_point, angle=angle, length=length)
#
# def draw_branches(point, angle, length):
#     if length <= 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle - 30, length=length)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
#     v2.draw()
#     """Попытка через for, но кто знал что окажется намного легче
#     (честно, задача прикольная, но повторять её не стану)"""
#     # list_of_point = [v1.end_point, v2.end_point]
#     # list_of_angle = [v1.angle, v2.angle]
#     # for point in list_of_point:
#     #     for angle in list_of_angle:
#     #         draw_branches(point, angle, length)
#     length = length * 0.75
#
#     """Я думал что через for перебором будет лучше, но просто из-за
#     того что мне приходилось каждый раз перебирать угол, дерево выходило слишком плотным и большим,
#     и поэтому я решил попробовать внутри функции вызывать себя два раза"""
#     draw_branches(point=v1.end_point, angle=v1.angle, length=length)
#     draw_branches(point=v2.end_point, angle=v2.angle, length=length)
#     """Это оказалось удобнее, по сути я не перебирал лишний углы к веткам, так ещё веток стало меньше"""
#
# draw_branch(sd.get_point(700, 0), angle=90, length=200)
# """Как итог скажу, задача того стоила, надо было просто понять саму суть и разобраться"""
# """Только на скриншоте преподавателя разрешение поменьше и я хз как он так сделал"""

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

sd.resolution = (1400, 1000)
def draw_branch(start_point, angle, length):
    v = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v.draw()
    draw_branches(point=v.end_point, angle=angle, length=length)

def draw_branches(point, angle, length):
    if length <= 10:
        return
    random_angle = sd.random_number(18, 42)
    random_length_int = sd.random_number(6, 9)
    random_length = random_length_int / 10
    v1 = sd.get_vector(start_point=point, angle=angle - random_angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle + random_angle, length=length)
    v2.draw()
    length = length * random_length
    draw_branches(point=v1.end_point, angle=v1.angle, length=length)
    draw_branches(point=v2.end_point, angle=v2.angle, length=length)

draw_branch(sd.get_point(700, 0), angle=90, length=200)

# Пригодятся функции
# sd.random_number()

sd.pause()
