import math
def checkBetween(a,b,c):
    ac,bc,ab = checkDistAngle(a,b)[0] ,checkDistAngle(b,c)[0] , checkDistAngle(a,c)[0]
    if ac + bc - ab < 0.0000001:
        return True
    return False 
    
def checkDistAngle(point1,point2):
    x1,y1 = point1  
    x2,y2 = point2
    dist = round((abs(x2 - x1)** 2 + abs(y2 - y1)** 2)** 0.5,10)
    angle = round(math.atan2((y2 - y1),(x2 - x1)),10)
    return dist,angle

def getAngleList(your_pos,list):
    AngList = []
    for l in list:
        dist,ang = checkDistAngle(your_position,l)
        AngList.append(ang)
    return AngList
    
def solution(dimensions, your_position, trainer_position, distance):
    count = 0
    w,h = dimensions
    x0,y0 = your_position
    x,y = trainer_position

    posX, posY  = [x],[y]
    posx, posy= x,y
    candidate, yourpos = [],[]
    
    n = max(w,h,distance)
    for r in range(100):
        if posx < n or posy < n:
            if r % 2 != 0:
                posx += 2*x
                posy += 2*y
            else:
                posx += 2*(w-x)
                posy += 2*(h-y)
            posX.append(posx)
            posY.append(posy)

    trainer = [[candidate.extend(((i,j),(i,-j),(-i,j),(-i,-j))) for i in posX] for j in posY]
    you = [[yourpos.extend(((i-(x-x0),j-(y-y0)),(i-(x-x0),-j+(y-y0)),(-i+(x-x0),j-(y-y0)),(-i+(x-x0),-j+(y-y0)))) for i in posX] for j in posY]
    newlist = []

    for i in range(len(candidate)):
        newlist.append(candidate[i])
        newlist.append(yourpos[i])

    selected_cand = []
    for cand in newlist:
        if 0 < checkDistAngle(cand,your_position)[0] <= distance:
            selected_cand.append(cand)
        
    HitList = []
    HitAngle = []
    
    for can in selected_cand:
        ang = checkDistAngle(can,your_position)[1]
        if not checkBetween(trainer_position,your_position,can) and ang not in HitAngle:# and checkCorner(i):
            HitAngle.append(ang)
            HitList.append(can)
            if can in candidate:
                count+=1
    return count

# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
# distance = 15

dimensions = [2,5]
your_position = [1,2]
trainer_position = [1,4]
distance = 100

# dimensions = [3, 2]
# your_position = [1, 1]
# trainer_position = [2, 1]
# distance = 4

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

