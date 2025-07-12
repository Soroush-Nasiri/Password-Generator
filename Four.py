import random

def Four_Numbers(length):
    A = random.randrange(1, length - 3)
    length -= A
    B = random.randrange(1, length - 2)
    length -= B
    C = random.randrange(1, length - 1)
    length -= C
    D = length
    return [A, B, C, D]