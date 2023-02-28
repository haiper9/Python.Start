import math

def task_1(text):
    result = {}
    text = text.strip('.')
    sentences = text.split('. ')
    for sentence in sentences:
        wordCount = len(sentence.split())
        result[sentence] = wordCount

    return result


def task_2(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)
