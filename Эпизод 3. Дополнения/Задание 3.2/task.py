import math
def task_1(a, search):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != search and low <= high:
        if search > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return str(mid)


def task_2(input_number):
    is_prime = True
    for i in range(2, int(math.sqrt(input_number))):
        if input_number % i != 0:
            is_prime = False

    return is_prime