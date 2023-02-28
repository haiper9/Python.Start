def task_1(input_list):
    return max(input_list, key=input_list.count)

def task_2(x, y):
    n = 8
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return 'NO'
    else:
        return 'YES'


def task_3(x, y, xc, yc, r):
    return ((x - xc) ** 2 + (y - yc) ** 2) <= (r * r)


def task_4(input_list):
    count = 0
    for i in range(1, len(input_list) - 1):
        if input_list[i - 1] < input_list[i] > input_list[i + 1]:
            count += 1
    return count


def task_5(key):
    data = open("file.txt", "r").read()
    rows = data.split('\n')
    newRows = []
    for row in rows:
        if '' == row:
            continue
        row = row.lower()
        newRow = ''
        for char in row:
            if char.isalpha():
                newChar = chr((ord(char) + key - 96) % 26 + 96)
            else:
                newChar = chr((ord(char) + key) + 64)
            newRow += newChar
        newRows.append(newRow)
    return newRows