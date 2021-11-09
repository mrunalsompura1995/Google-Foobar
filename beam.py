import math
import time

def current_milli_time():
    return round(time.time() * 1000)

def checkBetween(a,b,c):
    # checks if b is in between a and c
    ac,bc,ab = checkDistAngle(a,b)[0] ,checkDistAngle(b,c)[0] , checkDistAngle(a,c)[0]
    if ac + bc - ab < 0.0000001:
        return True
    return False 
    
def checkDistAngle(point1,point2):
    # distance and angle between point1 and point2
    x1,y1 = point1  
    x2,y2 = point2
    dist = round((abs(x2 - x1)** 2 + abs(y2 - y1)** 2)** 0.5,10)
    angle = round(math.atan2((y2 - y1),(x2 - x1)),10)
    return dist,angle
    
def solution(dimensions, your_position, trainer_position, distance):
    count = 0
    w,h = dimensions
    x0,y0 = your_position
    x,y = trainer_position

    posX, posY , posX0, posY0 = [x],[y],[x0],[y0]
    posx, posy, posx0, posy0 = x,y,x0,y0
    posXY,posXY0 = [(x,y)],[(x0,y0)]
    candidate, yourpos = [],[]
    list1 = []
    
    n = max(w,h,distance)
    for r in range(100):
        if posx < n or posy < n:
            if r % 2 != 0:
                posx += 2*x
                posy += 2*y
                posx0 += 2*x0 
                posy0 += 2*y0
            else:
                posx += 2*(w-x)
                posy += 2*(h-y)
                posx0 += 2*(w-x0)
                posy0 += 2*(h-y0)
            posX.append(posx)
            posY.append(posy)
            posX0.append(posx0)
            posY0.append(posy0)

    trainer = [[candidate.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in posX] for j in posY]
    you = [[yourpos.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in posX0] for j in posY0]
    
    newlist = []
    for i in range(len(candidate)):
        newlist.append(candidate[i])
        newlist.append(yourpos[i])
    
    selected_cand = [cand for cand in newlist if 0 < checkDistAngle(cand,your_position)[0] <= distance]
    
    HitList = []
    HitAngle = []
    
    for can in selected_cand:
        ang = checkDistAngle(can,your_position)[1]
        if not checkBetween(trainer_position,your_position,can) and ang not in HitAngle:
            HitAngle.append(ang)
            HitList.append(can)
            if can in candidate:
                count+=1
    return count

from math import atan2
from itertools import product

def solutions(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()
    for position in your_position, trainer_position:
        # print('p',position)
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            # print(reflect)
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                # print(x,y)
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative travel so we can filter later
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])

dimensions = [3,3]
your_position = [1,1]
trainer_position = [2,2]
# distance = 10

# dimensions = [2,5]
# your_position = [1,2]
# trainer_position = [1,4]
# distance = 100

# dimensions = [300, 275]
# your_position = [150, 150]
# trainer_position = [180, 100]
# distance = 500

# dimensions = [9,9]
# your_position = [3,3]
# trainer_position = [6,6]
# distance = 10

# dimensions = [10,10]
# your_position = [2,7]
# trainer_position = [9,9]
# distance = 60

# dimensions = [23,10]
# your_position = [6, 4]
# trainer_position = [3,2]
# distance = 23

# dimensions = [3, 2]
# your_position = [1, 1]
# trainer_position = [2, 1]
for d in range(100):
    t1 = current_milli_time()
    test = solution(dimensions,your_position,trainer_position,d)
    t2 = current_milli_time()
    soln = solutions(dimensions,your_position,trainer_position,d)
    t3 = current_milli_time()
    print('d',d,'test',test,'time',t2-t1,'soln',soln,'time',t3-t2)
    if test != soln:
        print('Error at ', d)
        break