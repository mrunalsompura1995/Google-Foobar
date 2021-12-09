import itertools as iter
from collections import defaultdict, Counter
import time

def current_milli_time():
    return round(time.time()*1000000)

# g = [[False,True,False,False],[False,False,True,False],[False,False,False,True],[True,False,False,False]]
g = [[True, True, False, True, False, True, False, True, True, False],
     [True, True, False, False, False, False, True, True, True, False],
     [True, True, False, False, False, False, False, False, False, True],
     [False, True, False, False, False, False, True, True, False, False]]
# g = [[True, False, True], [False, True, False], [True, False, True]]

kernel = [(((0,0),(0,0)),((1,1),(1,1)),((1,1),(0,0)),((0,0),(1,1)),((1,0),(0,1)),((0,1),(1,0)),
           ((1,1),(1,0)),((1,1),(0,1)),((1,0),(1,1)),((0,1),(1,1)),((0,1),(0,1)),((1,0),(1,0))),
          (((1,0),(0,0)),((0,1),(0,0)),((0,0),(1,0)),((0,0),(0,1)))] 

def calculate(column):
    grid = kernel[column[0]]
    for val in column[1:]:
        grid = (iter.chain.from_iterable([[(val2) + (val1[1],) for val1 in kernel[val] if val2[-1] == val1[0]] for val2 in grid]))
    return ([tuple(zip(*g)) for g in grid])

def solution(g):
    image = tuple(zip(*g))
    column_dict = dict(Counter([i[1] for i in calculate(image[0])]))
    for column in image[1:]:
        list1,list2 = [],[]
        for c in calculate(column):
            if c[0] in column_dict:
                if c[1] in list1: 
                    list2[list1.index(c[1])]+=column_dict[c[0]] 
                else:
                    list1.append(c[1])
                    list2.append(column_dict[c[0]])
        column_dict = dict(zip(list1,list2))
    return sum(column_dict.values())

print(solution(g))
