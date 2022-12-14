in_path = 'day1-input.txt'

''' solution 1 using numpy '''
import numpy as np

# amount of elements that are larger than their previous
def p1(depths):
    return (np.diff(depths) > 0).sum()

# comparing sliding windows of length n instead
def p2(depths, n):

    # convolution to generate the sliding windows
    return p1(np.convolve(depths, np.ones(n), 'valid'))

# preprocess input. loading the whole file?? smh
with open(in_path) as infile:
    inputs = np.array(infile.read().splitlines()).astype(int)

# parts. All answers are off by 1 smhh
print("part 1:", p1(inputs))
print("part 2:", p2(inputs, 3))

