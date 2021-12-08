import numpy as np
from itertools import permutations
import itertools as iter
from collections import defaultdict, Counter

# g = [[False,True,False,False],[False,False,True,False],[False,False,False,True],[True,False,False,False]]
# g = [[True, True, False, True, False, True, False, True, True, False],
#      [True, True, False, False, False, False, True, True, True, False],
#      [True, True, False, False, False, False, False, False, False, True],
#      [False, True, False, False, False, False, True, True, False, False]]
g = [[True, False, True], [False, True, False], [True, False, True]]

kernel = [(((0,0),(0,0)),((1,1),(1,1)),((1,1),(0,0)),((0,0),(1,1)),((1,0),(0,1)),((0,1),(1,0)),
          ((1,1),(1,0)),((1,1),(0,1)),((1,0),(1,1)),((0,1),(1,1)),((0,1),(0,1)),((1,0),(1,0))),
          (((1,0),(0,0)),((0,1),(0,0)),((0,0),(1,0)),((0,0),(0,1)))] 

def calculate(column):
    grid = kernel[column[0]]
    for val in list(column)[1:]:
        grid = tuple(iter.chain.from_iterable([[(val2)+(val1[1],) for val1 in kernel[val] if val2[-1]==val1[0]] for val2 in grid]))
    return tuple([tuple(zip(*g)) for g in grid])

def solution(g):
    image = tuple(zip(*g))
    preimgs =  defaultdict(int)
    for im in calculate(image[0]):
        preimgs[im[1]]+=1
    for tuples in list(image)[1:]:
        nxt_preimages = {}
        for p in calculate(tuples):
            if p[0] in preimgs:
                nxt_preimages[p[1]] = preimgs[p[0]] + (nxt_preimages[p[1]] if p[1] in nxt_preimages else 0)
        preimgs = nxt_preimages
    return sum(preimgs.values())

print(solution(g))
