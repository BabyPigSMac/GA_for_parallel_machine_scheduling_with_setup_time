import random


def cal_break_point(length):
    first_point = random.randint(1, length - 1)
    second_point = random.randint(1, length - 1)
    while first_point == second_point:
        second_point = random.randint(1, length - 1)
    break_point = [first_point, second_point]
    break_point.sort()
    return break_point
