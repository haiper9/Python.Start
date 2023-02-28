import math

def task_1(a, d, c):
    return (c - d / 5 + (321 ** 0.5)) / (1 + 3 * a)


# Пример 2
def task_2(a, d, c):
    return (math.log10(c / 3) - d + 25) / (5 * a - 1)


# Пример 3
def task_3(a, d, c):
    return (c / 2 + math.log(d) - 35) / (5 * a + 1)


# Пример 4
def task_4(a, d, c):
    return (math.tan(c) + d / 32) / (a / 3 + 1)


# Пример 5
def task_5(a, d, c):
    return (c / 5 - d + 1) / (c + math.tan(2 * a))


# Пример 6
def task_6(a, d, c):
    return (((25 * c) ** 0.5) + d - 3) / (d - a ** 2 + 1)


# Пример 7
def task_7(a, d, c):
    return (5 * math.log10(c) + 3 * d - 32) / (a ** 2 + 1)


# Пример 8
def task_8(a, d, c):
    return (c * d - math.log(4 * 3 * a)) / (c + a - 1)