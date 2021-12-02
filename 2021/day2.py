in_path = 'day2-input.txt'

import numpy as np
import re
from functools import reduce

def p1(data):
    return np.add.reduce(data)

def p2(data):

    # [horizontal(a+b), aim(a+b), (depth(a) + aim(a+b) * horizontal(b))]
    f = lambda a, b: [a[0]+b[0], a[1]+b[1], a[2] + (a[1] + b[1])*b[0]]
    return reduce(f, data, np.array([0,0,0]))

def to_vector(x, basis):
    dir, size = re.split('\s+', x.strip())
    return np.multiply(basis[dir[0]], int(size))  

# preprocessing yum
movement_vectors = {"u" : [0,-1],
                    "d" : [0, 1],
                    "f" : [1, 0]}

with open(in_path) as infile:
    data = infile.read().splitlines()

movements = [to_vector(x, movement_vectors) for x in data]

# parts
p_1, p_2 = p1(movements), p2(movements)
print(p_1[0]*p_1[1])
print(p_2[0]*p_2[2])

