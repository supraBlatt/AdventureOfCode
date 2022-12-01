in_path = 'day3-input.txt'

import numpy as np

def to_int(bin):
    return bin.dot(1 << np.arange(bin.size)[::-1])

def freq_bin(data, axis=None):
    

# everything here is absolutely wrong in case all of the column is the same
def frequent(data, axis=None):
    return (np.mean(data, axis=axis) >= 0.5)

def p1(data):
    gamma = frequent(data, 0)
    return to_int(gamma) * to_int(np.invert(gamma))

# iterative solution = no big numpy = sadge
def p2(data, mode):
    pass    
# preprocess into a matrix of binary  digits
data = np.genfromtxt(in_path, delimiter=1, dtype=np.int8)

# parts

print("part 1:", p1(data))
print(p2(data, 0) * p2(data, 1))

