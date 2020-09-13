# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
sd.resolution = (1200, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x, y, color):
    point = sd.get_point(x,y)
    sd.circle(point, radius=50, color=color, width=1)

    left_eye = sd.get_point(x-20, y+20)
    right_eye = sd.get_point(x+20, y+20)
    sd.circle(left_eye, radius=5, color=color, width=1)
    sd.circle(right_eye, radius=5, color=color, width=1)

    mouth = (sd.get_point(x-20, y-10), sd.get_point(x, y), sd.get_point(x+20,y-10))
    sd.lines(point_list=mouth, color=color, closed=False, width=1)

for _ in range(10):
    point = sd.random_point()
    # print(point[])
    smile(sd.random_number(0, 600), sd.random_number(0, 600), sd.COLOR_RED)
sd.pause()
