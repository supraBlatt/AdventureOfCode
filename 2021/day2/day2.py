in_path = 'day2-input.txt'

import numpy as np
import re
from functools import reduce

def p1(data):
    return np.prod(np.add.reduce(data))

def p2(data):

    # [horizontal(a+b), aim(a+b), (depth(a) + aim(a+b) * horizontal(b))]
    f = lambda a, b: [a[0]+b[0], a[1]+b[1], a[2] + (a[1] + b[1])*b[0]]
    return reduce(f, data, [0,0,0])

def t_p2(data):
    # cumulative sum of aims * horiziontal movements = depth
    # return depth * overall horizontal movement
    # credit to shadow
    return (np.cumsum(data[:,1])*data[:,0]).sum() * data[:,0].sum()

def to_vector(x, basis):
    dir, size = re.split('\s+', x.strip())
    return np.multiply(basis[dir[0]], int(size))  

# preprocessing yum
moves = {"u" : [0,-1],
         "d" : [0, 1],
         "f" : [1, 0]}

with open(in_path) as infile:
    data = infile.read().splitlines()

# transofrm all movements to stuff like 'forward 10' -> [10, 0]
# 'up 15' -> [0, -15]
movements = np.array([to_vector(x, moves) for x in data])


# parts
p_2 = p2(movements)
print("part 1:", p1(movements))
print("part 2:", p_2[0]*p_2[2])
print("shadow part 2:", t_p2(movements))

