import numpy as np
from collections.abc import Iterator
import heapq

INPUT = 'input.txt'
# --------------------------------------------------------------

'''  naive approaches ''' 
def parse() -> list[int]:
    overall = []
    with open(INPUT) as file: 
        # split to blocks by blank line
        for block in file.read().split('\n\n'):
            # split each block by newline and sum them
            calorie_sum = sum(map(int, block.split('\n'))) 
            overall.append(calorie_sum)
    return overall

def p1(input: list[int]) -> int: 
    return max(input)

def p2(input: list[int]) -> int: 
    return sum(sorted(input, reverse=True)[:3])

# --------------------------------------------------------------

''' an awful attempt at lazy evaluation'''
def lazy_parse() -> Iterator[int]: 
    with open(INPUT) as file:
        sum = 0
        for line in file: 
            # split by blank line - to blocks of sums
            if line.strip(): 
                sum += int(line.strip())
            else:
                yield sum
                sum = 0
        # yield last sum
        if sum: 
            yield sum

def lazy_p1() -> int: 
    # return the maximum element of the blocks
    return max(lazy_parse()) 

def alt_p2(n: int) -> int:
    # returns the maximum 3 elements of the blocks
    # lmao i have 0 idea how this works.
    # i don't even think it's lazy. it takes an iterable and spits out a list.
    return sum(heapq.nlargest(n, lazy_parse()))

# --------------------------------------------------------------

''' running '''
calories = parse()
print(f"naive part 1: {p1(calories)}")
print(f"naive part 2: {p2(calories)}")
print(f"lazy ass part 1: {lazy_p1()}")
print(f"wannabe lazy ass part2: {alt_p2(3)}")
