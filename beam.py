import math

def geometry(point1,point2):
    x1,y1 = point1  
    x2,y2 = point2
    dist = (abs(x2 - x1)** 2 + abs(y2 - y1)** 2)** 0.5
    angle = math.atan2((x1 - x2),(y1 - y2))
    return dist,angle

def solution(dimensions, your_position, trainer_position, distance):
    count = 0
    w,h = dimensions
    x,y = trainer_position
    x0,y0 = your_position
    d = distance

    ListX, ListY , ListX0, ListY0 = [x],[y],[x0],[y0]
    posx, posy, posx0, posy0 = x, y, x0, y0
    trainers, yourpos = [],[]
    Data = {}

    n = max(d,50)
    for r in range(n):
        if (len(ListX) < (d//w)+1)  or (len(ListY) < (d//h)+1):
            if r % 2 == 0:
                posx += 2*(w-x)
                posy += 2*(h-y)
                posx0 += 2*(w-x0)
                posy0 += 2*(h-y0)
            else:
                posx += 2*x
                posy += 2*y
                posx0 += 2*x0 
                posy0 += 2*y0
            ListX.append(posx)
            ListY.append(posy)
            ListX0.append(posx0)
            ListY0.append(posy0)

    list1 = [[trainers.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in ListX] for j in ListY]
    list2 = [[yourpos.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in ListX0] for j in ListY0]
    
    for position in yourpos,trainers:
        for pos in position:
            dist,angle = geometry(your_position,pos)
            if dist > d or angle in Data and dist > Data[angle]:
                continue
            if position == trainers:
                count+=1
            Data[angle] = dist
    return count


### Test Cases:

# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
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

dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
distance = 4

# print(solution(dimensions,your_position,trainer_position,distance))

