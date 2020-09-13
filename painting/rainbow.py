# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код


# step = 5
# for i in rainbow_colors:
#     start_point = sd.get_point(50, 50-step)
#     end_point = sd.get_point(350, 450-step)
#     sd.line(start_point=start_point, end_point=end_point, color=i, width=4)
#     step += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
def rainbow():
    step = 30
    for color in rainbow_colors:
        point = sd.get_point(0, 0)
        sd.circle(center_position=point, radius=1200-step, color=color, width=10)
        step += 10
rainbow()
