def solution(dimensions, your_position, trainer_position, distance):
    count = 0
    w,h = dimensions
    x0,y0 = your_position
    x,y = trainer_position
    def checkCorner(candidate):
        slope = 0
        if x - x0 != 0:
            slope = abs(y - y0) / abs(x - x0)
        x1,y1 = candidate
        if (x1,y1) == (x,y):
            return True
        corner = (y1-y0) == slope * (x1 - x0)
        if corner == True:
            return False
        a = checkDistance(your_position,candidate) 
        b = checkDistance(your_position,trainer_position)
        c = checkDistance(candidate,trainer_position)
        if b + c == a or a+ b == c:
            return False
        return True

    def checkDistance(point1,point2):
        x1,y1 = point1
        x2,y2 = point2
        return (abs(x2 - x1)** 2 + abs(y2 - y1)** 2)** 0.5

    posX = []
    posY = []
    candidate = []
    for i in range(50):
        if i % 2 != 0:
            posx += 2*(w-x)
            posy += 2*(h-y)
        else:
            if i == 0:
                posx = x
                posy = y
            else:
                posx += 2*x
                posy += 2*y
        posX.append(posx)
        posY.append(posy)

    pos = [[candidate.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in posX] for j in posY]
    for i in candidate:
        if checkDistance(i,your_position) <= distance and checkCorner(i):
            count+=1
    return count

# import math

# def solution(dimensions, your_position, trainer_position, distance):
#     count = 0
#     w,h = dimensions
#     x0,y0 = your_position
#     x,y = trainer_position

#     def checkDistance(point1,point2):
#         x1,y1 = point1  
#         x2,y2 = point2
#         dist = round((abs(x2 - x1)** 2 + abs(y2 - y1)** 2)** 0.5,5)
#         angle = round(math.atan2((y2 - y1),(x2 - x1)),5)
#         return dist,angle

#     def checkBetween(a,b,c):
#         for i in c:
#             ac,bc,ab = checkDistance(a,i)[0] , checkDistance(i,b)[0] , checkDistance(a,b)[0]
#             if ac + bc - ab < 0.001:
#                 return False
#         return True       

#     def getAngleList(your_position, yourpos):
#         angList = []
#         for pos in yourpos:
#             dist,ang = checkDistance(your_position,pos)
#             angList.append(ang)
#         return angList
    
#     posX, posY , posX0, posY0 = [x],[y],[x0],[y0]
#     posx, posy, posx0, posy0 = x,y,x0,y0
#     candidate, yourpos = [],[]

#     for r in range(50):
#         if r % 2 != 0:
#             posx += 2*x
#             posy += 2*y
#             posx0 += 2*x0 
#             posy0 += 2*y0
#         else:
#             posx += 2*(w-x)
#             posy += 2*(h-y)
#             posx0 += 2*(w-x0)
#             posy0 += 2*(h-y0)
#         posX.append(posx)
#         posY.append(posy)
#         posX0.append(posx0)
#         posY0.append(posy0)

#     trainer = [[candidate.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in posX] for j in posY]
#     you = [[yourpos.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in posX0] for j in posY0]
#     yourpos.remove((x0,y0))
#     finallist =  yourpos + candidate
#     hitlist = []
#     AngleList = set(getAngleList(your_position,yourpos))
#     print(AngleList)
#     for c in finallist:
#         dist,ang = checkDistance(your_position,c)
#         # print(c,ang,dist)
#         if dist <= distance and checkBetween(your_position,c,hitlist):
#             hitlist.append(c)
#             if c in candidate:
#                 count+=1
#     # print(hitlist)
#     return count

# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
# distance = 15

dimensions = [2,5]
your_position = [1,2]
trainer_position = [1,4]
distance = 11

# dimensions = [3, 2]
# your_position = [1, 1]
# trainer_position = [2, 1]
# distance = 5

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

print(solution(dimensions,your_position,trainer_position,distance))

