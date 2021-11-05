from itertools import product
from math import atan2
from numpy import ones,vstack
from numpy.linalg import lstsq

def solution(dimensions, your_position, trainer_position, distance):
    count = 0
    w,h = dimensions
    x0,y0 = your_position
    x,y = trainer_position

    def checkCorner(candidate):
        points = [(x0,y0),(x,y)]
        x_coords, y_coords = zip(*points)
        A = vstack([x_coords,ones(len(x_coords))]).T
        m, c = lstsq(A, y_coords)[0]
        check_x,check_y = candidate
        if check_y == int(m) * check_x + int(c):
            return True
        else:
            return False

    def checkDistance(candidate):
        m,n = candidate 
        d = (abs(m - x0) ** 2 + abs(n - y0) ** 2) ** 0.5
        return d

    p,q = 4,4
    candidate = p,q
    dist = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
    if checkDistance(candidate) < distance and checkCorner(candidate):
        count+=1
    print(dist,count)



dimensions = [3,3]
your_position = [1,1]
trainer_position = [2,2]
distance = 5
print(solution(dimensions,your_position,trainer_position,distance))
    