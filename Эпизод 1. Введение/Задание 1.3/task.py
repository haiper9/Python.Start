def task_1(n):
    result = 0
    i=1
    while i<11:
        result+=1/i
        i=i+1
    return result


# Пример 2
def task_2(x, n):
    result = 0
    i = 1
    while i < 18:
        result += x / i
        i = i + 2
    return result


# Пример 3
def task_3(n):
    result = 1
    i = 1
    while i < n+1:
        result *= i
        i = i + 1
    return result


# Пример 4
def task_4(x, n):
    result = 1
    i = 2
    while i < n+1:
        result *= (x+i)/i
        i = i + 1
    return result


# Пример 5
def task_5(x, n):
    result = 0
    i=1
    while i<n+1:
        result+=x/2
        i=i+1
    return result


# Пример 6
def task_6(n):
    result = 1
    i = 2
    while i < 21:
        result *= i
        i = i + 2
    return result