# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
size_of_brick = {'x': 40, 'y': 10}
size_of_house = {'x': 500, 'y': 200}
begin = {'x': 200, 'y': 100}


def build_house(begin, size_of_house):
    for y in range(begin['y'], begin['y'] + size_of_house['y'] - size_of_brick['y'], size_of_brick['y'] * 2):
        for x in range(begin['x'], begin['x'] + size_of_house['x'] - size_of_brick['x'], size_of_brick['x']):
            point_left = sd.get_point(x, y)
            point_right = sd.get_point(x + size_of_brick['x'], y + size_of_brick['y'])
            sd.rectangle(left_bottom=point_left, right_top=point_right, color=sd.COLOR_DARK_RED, width=2)

            point_left2 = sd.get_point(x + size_of_brick['x'] / 2, y + size_of_brick['y'])
            point_right2 = sd.get_point(x + size_of_brick['x'] * 1.5, y + size_of_brick['y'] * 2)
            sd.rectangle(left_bottom=point_left2, right_top=point_right2, color=sd.COLOR_DARK_RED, width=2)

        point_left3 = sd.get_point(begin['x'] + size_of_house['x'] - size_of_brick['x'] / 2, y)
        point_right3 = sd.get_point(begin['x'] + size_of_house['x'], y + size_of_brick['y'])
        sd.rectangle(left_bottom=point_left3, right_top=point_right3, color=sd.COLOR_DARK_RED, width=2)

        point_left4 = sd.get_point(begin['x'], y + size_of_brick['y'])
        point_right4 = sd.get_point(begin['x'] + size_of_brick['x'] / 2, y + size_of_brick['y'] * 2)
        sd.rectangle(left_bottom=point_left4, right_top=point_right4, color=sd.COLOR_DARK_RED, width=2)

def ground():
    sd.vector(sd.get_point(0, 0), 0, 1200, color=sd.COLOR_DARK_GREEN, width=200)

def roof(begin, end, height):
    points_list = []
    points_list.append(sd.get_point(begin['x'], begin['y']))
    points_list.append(sd.get_point(end['x'], end['y']))
    points_list.append(sd.get_point((end['x'] + begin['x']) / 2, end['y'] + height))
    sd.polygon(point_list=points_list, color=(59, 15, 15), width=0)
    # print(points_list)


point0 = {'x': begin['x'], 'y': begin['y'] + size_of_house['y']}
point1 = {'x': begin['x'] + size_of_house['x'], 'y': begin['y'] + size_of_house['y']}
#
build_house(begin, size_of_house)
roof(point0, point1, 100)
ground()
# sd.pause()
