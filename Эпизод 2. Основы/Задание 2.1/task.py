def task_1(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result
    return


def task_2(N):
    a = 1
    b = 1
    for i in range(1, N + 1):
        b = a + b
    return b
    return


def task_3(N):
    dividers = []
    for i in range(1, N + 1):
        if N % i == 0:
            dividers.append(i)

    return dividers
    return
